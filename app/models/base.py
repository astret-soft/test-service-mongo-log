""" Base model
"""

__all__ = ('BaseModel',)


class BaseModel:
    """ Base model
    """

    def __init__(self, app):
        self.collection = app.db[self.__class__.__name__.lower()]

    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            return object.__getattribute__(self.collection, name)
