import json

from aiohttp.web import HTTPOk
from jsonschema import validate

from api.db import db
from api.main import get_app_for_tests


__all__ = ('BasicApiTestCaseMixin', 'CommonSearchTestCaseMixin')


class BasicApiTestCaseMixin:
    fixtures = None

    async def get_application(self):
        return get_app_for_tests()

    async def setUpAsync(self):
        await db.clear_all()
        for x in self.fixtures or []:
            with open(str(x)) as f:
                db.load_fixtures(json.load(f))
