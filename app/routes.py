""" Routes
"""
from aiohttp.web import RouteTableDef

__all__ = ('setup_routes', 'routes')

routes = RouteTableDef()


def setup_routes(app):
    """ Setup all routes
    """
    app.add_routes(routes)
