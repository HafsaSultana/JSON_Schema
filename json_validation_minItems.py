from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "scores": {
            "type": "array",
            "items": {"type": "number"},
            "minItems": 1
        },
    },
    "required": ["name"],
}

validate(instance={"name": "John", "age": 30, "scores": []}, schema=schema)
# ValidationError: [] is too short

# validate(instance={"name": "John", "age": 30, "scores": [5]}, schema=schema)
# # No error, the JSON is valid.
