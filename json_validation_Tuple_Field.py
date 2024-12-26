from jsonschema import validate

# Tuple defined with draft 2019-09:
# schema_2019_09 = {
#     "$schema": "https://json-schema.org/draft/2019-09/schema",  # This must be specified.
#     "type": "object",
#     "properties": {
#         "name": {"type": "string"},
#         "age": {"type": "number"},
#         "scores": {
#             "type": "array",
#             "items": [{"type": "number"}, {"type": "number"}],
#             "minItems": 2,
#             "additionalItems": False,
#         },
#     },
#     "required": ["name"],
# }

# validate(
#     instance={"name": "John", "age": 30, "scores": [70, 80, 90]},
#     schema=schema_2019_09,
# )
# # ValidationError: Additional items are not allowed (90 was unexpected)

###_________________________________________________________________###

# Tuple defined with draft 2020-12:
schema_2020_12 = {
    "$schema": "https://json-schema.org/draft/2020-12/schema", # This is the default and thus optional.
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "scores": {
            "type": "array",
            "prefixItems": [{"type": "number"}, {"type": "number"}],  # Use prefixItems rather than items.
            "minItems": 2,
            "items": False, # Use items rather than additionalItems.
        },
    },
    "required": ["name"],
}

validate(
    instance={"name": "John", "age": 30, "scores": [70, 80, 90]},
    schema=schema_2020_12,
)
# ValidationError: Expected at most 2 items, but found 3
