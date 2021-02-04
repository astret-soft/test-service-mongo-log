""" REST API service to store logs in mongodb and collect them from WS
"""
import asyncio
import uvloop

from aiohttp import web

from app.collect_logs import setup_collect_logs
from app.db import setup_db
from app.routes import setup_routes
from app.settings import HOST, PORT
from app.views import *  # pylint: disable = wildcard-import, unused-wildcard-import


def get_app():
    """ Setup and get application
    """
    app_ = web.Application()
    for setup in (setup_routes, setup_db, setup_collect_logs):
        setup(app_)
    return app_


if __name__ == "__main__":
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    web.run_app(get_app(), host=HOST, port=PORT)
