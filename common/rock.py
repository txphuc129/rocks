from jsonschema import validate

from common.constants import DENSITY, ENERGY, FAMILY, PALETTE, RADIUS, RADIUS0, RADIUS1


class Voronoi:
    def __init__(self):
        self._id = ''
        self._properties = {}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        validate(instance=value, schema={'type': 'string'})
        self._id = value

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        validate(instance=value, schema=voronoi_schema)
        self._properties = value


class Metaball:
    def __init__(self):
        self._id = ''
        self._properties = {}

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        validate(instance=value, schema={'type': 'string'})
        self._id = value

    @property
    def properties(self):
        return self._properties

    @properties.setter
    def properties(self, value):
        validate(instance=value, schema=metaball_schema)
        self._properties = value


voronoi_schema = {
    'type': 'object',
    'properties': {
        FAMILY: {'type': 'string'},
        DENSITY: {'type': 'number'},
        RADIUS: {'type': 'number'},
        PALETTE: {
            'type': 'array',
            'items': {
                'type': 'array',
                'items': {
                    'type': 'number'
                }
            }
        },
    },
    'required': [FAMILY, DENSITY, RADIUS, PALETTE],
    'additionalProperties': False
}

metaball_schema = {
    'type': 'object',
    'properties': {
        FAMILY: {'type': 'string'},
        DENSITY: {'type': 'number'},
        RADIUS0: {'type': 'number'},
        RADIUS1: {'type': 'number'},
        ENERGY: {'type': 'number'}
    },
    'required': [FAMILY, DENSITY, RADIUS0, RADIUS1, ENERGY],
    'additionalProperties': False
}
