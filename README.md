# JSON Schema Validator: A Quick Overview

JSON Schema Validator is a tool that ensures JSON data conforms to a predefined schema. It validates the structure, data types, and constraints of JSON, enabling developers to maintain consistent and error-free data.

---

## Key Features
- **Validation of Data Structure**: Ensures that JSON objects follow the specified hierarchy and relationships.
- **Type Checking**: Verifies that each field in the JSON has the correct data type (e.g., string, number, array).
- **Custom Constraints**: Supports constraints like minimum/maximum values, string lengths, and required fields.
- **Extensibility**: Allows defining custom formats and reusable components using `$ref`.

---

## JSON Schema Components
- **`$schema`**: Defines the version of the JSON Schema (e.g., Draft 2020-12).
- **`type`**: Specifies the data type (e.g., `object`, `array`, `string`).
- **`properties`**: Lists the fields of an object with their constraints.
- **`required`**: Marks specific fields as mandatory.
- **`items`**: Defines the structure of elements in an array.
- **`enum`**: Restricts a value to a set of predefined options.

---

## Example
### Schema
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number", "minimum": 0 },
    "email": { "type": "string", "format": "email" }
  },
  "required": ["name", "age"]
}
