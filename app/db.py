""" Database
"""
from motor.motor_asyncio import AsyncIOMotorClient

from app.settings import MONGODB_HOST

__all__ = ('setup_db',)


async def startup(app):
    """ Start up database
    """
    app.db = AsyncIOMotorClient(
        MONGODB_HOST,
        io_loop=app.loop,
    )['vehicle_logs']


async def cleanup(app):
    """ Close database
    """
    app.db.close()


def setup_db(app):
    """ Setup database for application
    """
    app.on_startup.append(startup)
    app.on_cleanup.append(cleanup)
    return app
