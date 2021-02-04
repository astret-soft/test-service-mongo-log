""" Retrieve vehicle logs
"""

from aiohttp.web import json_response, View

from app.routes import routes
from app.models import VehicleLog
from views.mixins import PagingWithLastViewMixin

__all__ = ('RetrieveLogsView',)


@routes.view('/logs', name='logs-view')
class RetrieveLogsView(PagingWithLastViewMixin, View):
    """ Retrieve logs
    """

    async def get(self):
        limit, offset, last = await self.parse_paging()

        cursor = (
            VehicleLog(self.request.app).find().skip(offset).limit(limit) if last is None
            else VehicleLog(self.request.app).find({'_id': {'$gt': last}}).skip(offset).limit(limit)
        )

        result = [VehicleLog.to_representation(x) async for x in cursor]

        return json_response({
            'length': len(result),
            'limit': limit,
            'offset': offset,
            'last': result[-1]['id'] if result else None,
            'result': result,
        })
