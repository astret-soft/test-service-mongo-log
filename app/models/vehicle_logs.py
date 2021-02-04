""" Vehicle log
"""

from .base import BaseModel


class VehicleLog(BaseModel):
    """ Vehicle log
    """

    component: str
    country: str
    description: str
    model: str

    @staticmethod
    def to_representation(data: dict):
        """ Representation for REST API
        """
        _id = data.pop('_id')
        data['id'] = str(_id)
        data['timestamp'] = _id.generation_time.isoformat()
        data['country'] = data.get('country') or 'USA'
        return data
