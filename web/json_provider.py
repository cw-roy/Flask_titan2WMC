import orjson
from flask.json.provider import JSONProvider

class OrjsonProvider(JSONProvider):
    def dumps(self, obj, **kwargs):
        # Use orjson options for better performance and formatting
        options = orjson.OPT_INDENT_2 | orjson.OPT_SERIALIZE_NUMPY
        return orjson.dumps(obj, option=options).decode('utf-8')

    def loads(self, s, **kwargs):
        if isinstance(s, bytes):
            return orjson.loads(s)
        return orjson.loads(s.encode('utf-8'))