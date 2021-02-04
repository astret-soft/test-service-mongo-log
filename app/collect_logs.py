""" Task with listeting WS Server in background
"""

import logging
from json import loads, JSONDecodeError

from asyncio import create_task, sleep
from aiohttp import ClientSession, ClientTimeout, WSMsgType, ClientError

from app.settings import WS_LOG_SRC, WS_RETRIES_TIMEOUT
from app.models import VehicleLog

__all__ = ('setup_collect_logs',)

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING)


async def listen_ws_sub_logs(app):
    """ Listen WS Server for new logs and insert it into database
    """
    while True:
        try:
            async with ClientSession(
                    timeout=ClientTimeout(connect=WS_RETRIES_TIMEOUT, total=WS_RETRIES_TIMEOUT)
            ) as session:
                async with session.ws_connect(WS_LOG_SRC) as websocket:
                    async for msg in websocket:
                        if msg.type == WSMsgType.TEXT:
                            try:
                                data = loads(msg.data)
                                await VehicleLog(app).collection.insert_one(data)
                            except JSONDecodeError:
                                logger.warning('Bad JSON "%s"', msg.data)
                        elif msg.type == WSMsgType.ERROR:
                            break
        except ClientError as ex:
            logging.warning('During WS connection: "%s". Retries in %s seconds...', str(ex), WS_RETRIES_TIMEOUT)
            await sleep(WS_RETRIES_TIMEOUT)


async def startup(app):
    """ Start task with listening WS Server with logs
    """
    app.collect_logs = create_task(listen_ws_sub_logs(app))


async def cleanup(app):
    """ Stop task with listening WS Server with logs
    """
    app.collect_logs.cancel()
    await app.collect_logs


def setup_collect_logs(app):
    """ Setup task with listening WS Server with logs
    """
    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)
    return app
