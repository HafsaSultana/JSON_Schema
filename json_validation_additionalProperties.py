from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
    },
    "required": ["name"],
    "additionalProperties": False
}

validate(instance={"name": "John", "age": 30, "job": "Engineer"}, schema=schema)
# ValidationError: Additional properties are not allowed ('job' was unexpected)
