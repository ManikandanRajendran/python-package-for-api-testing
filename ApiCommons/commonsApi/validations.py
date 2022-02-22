from jsonschema import validate

def validate_status_code(response, expected_status):
    assert response.status_code == int(expected_status), f"Status code validation failed. Expected {expected_status}, Actual {response.status_code}"

def validate_strings(actual_message, expected_message):
    assert actual_message == expected_message, f"String validation failed. Expected {expected_message}, Actual {actual_message}"

def validate_schema(response, expected_schema):
    validate(instance=response, schema=expected_schema), "schema validation failed"

def value_present(response, expected_value):
    if type(response) != dict:
        response = response.json()
    assert expected_value in response, f"Attribute {expected_value} is not available"

def is_json(response):
    assert 'application/json' in response.headers.get('content-type'), "The response is not json value"
