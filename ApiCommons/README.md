# API Testing Commons

- This is a package to automate apis in a simple way by using common reusable functions.

- This module containes the major reusable functions which can be imported and accessed directly which will reduce the time and code redundancy.

## Installation
----------------

```
pip install commonsApi
```

## Methods available
---------------------
- > get_api(endpoint, header)
- > post_api(endpoint, request_payload, header)
- > put_api(endpoint, request_payload, header)
- > delete_api(endpoint, data, header)
- > patch_api(endpoint, request_payload, header)
- > validate_status_code(response, expected_status)
- > validate_schema(response, expected_schema)
- > validate_strings(actual_message, expected_message)
- > value_present(response, expected_value)
- > is_json(response)


## Sample code

```python
import commonsApi
url = "https://api.postcodes.io/random/postcodes"
header = {}
resp = commonsApi.get_api(url, header)
print(resp.json())
```

## Raise if any issues/changes needed
 Please raise an issue [here](https://github.com/ManikandanRajendran/python-package-for-api-testing/issues) if anything
