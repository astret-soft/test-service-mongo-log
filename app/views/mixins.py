""" Mixins for views
"""

from aiohttp.web import HTTPBadRequest
from bson import ObjectId

__all__ = ('PagingWithLastViewMixin',)


class PagingWithLastViewMixin:
    """ Mixin for paging in mongodb by id_
    """

    default_limit = 50
    max_limit = 1000

    async def parse_paging(self):
        """ Retrieve from query params limit, offset, last and validate them
        :return: limit, offset, last
        """
        try:
            limit = int(self.request.query.get('limit', self.default_limit))
            assert 0 < limit <= self.max_limit
        except (ValueError, AssertionError):
            raise HTTPBadRequest(reason=f'Invalid limit 0 < limit <= {self.max_limit}')

        try:
            offset = int(self.request.query.get('offset', 0))
            assert offset >= 0
        except (ValueError, AssertionError):
            raise HTTPBadRequest(reason='Invalid offset: offset >= 0')

        try:
            last = self.request.query.get('last')
            if last is not None:
                assert ObjectId.is_valid(last)
                last = ObjectId(last)
        except (ValueError, AssertionError):
            raise HTTPBadRequest(reason='Invalid last')

        return limit, offset, last
