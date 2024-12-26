from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "scores": {
            "type": "array",
            "items": {"type": "number"},
        },
        "address": {
            "type": "object",
            "properties": {
                "street": {"type": "string"},
                "postcode": {"type": "string"},
            },
            "required": ["street"],
        },
    },
    "required": ["name"],
}

validate(
    instance={
        "name": "John",
        "age": 30,
        "scores": [70, 90],
        "address": {"street": "Wall Street 1", "postcode": "NY 10005"},
    },
    schema=schema,
)
# No error, the JSON is valid.

validate(
    instance={
        "name": "John",
        "age": 30,
        "scores": [70, 90],
        "address": {"postcode": "NY 10005"},
    },
    schema=schema,
)
# ValidationError: 'street' is a required property
