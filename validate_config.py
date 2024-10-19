from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "DATA_SOURCES": {
            "type": "array",
            "items": { "type": "string" },
        },
        "FEEDBACK_LEVEL": {"type": "string"},
        "PASSWORD": {"type": "string"},
        "HIERARCHY": {
            "type": "array",
            "items": { "type": "string" },
        },
        "TIMESPAN": {
            "type": "object",
            "properties": {
                "START": {"type": "number"},
                "END": {"type": "number"},
            }
        },
        "DISPLAY": {
            "type": "object",
            "properties": {
                "INSTANCE_TITLE": {"type": "string"},
                "TIME_NAME": {"type": "string"},
                "NUMERICAL_NAME": {"type": "string"},
                "COMMENT_NAME": {"type": "string"},
            },
            "required": ["INSTANCE_TITLE", "TIME_NAME", "NUMERICAL_NAME", "COMMENT_NAME"],
        },
        "COLORS": {
            "type": "object",
            "properties": {
                "FARMERS": {"type": "string"},
                "SATELLITE": {"type": "string"}
            },
            "required": ["FARMERS", "SATELLITE"],
        },
    },
    "required": ["FEEDBACK_LEVEL", "PASSWORD", "HIERARCHY", "TIMESPAN", "DISPLAY", "COLORS"]
}

def validate_config(config):
    validate(instance=config, schema=schema)
