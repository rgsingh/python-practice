"""Compare two JSON objects by nested keys and values and ignore dynamic properties."""


def compare_json_objects(expected_json: dict or None, actual_json: dict or None) -> bool:
    ignore_keys = ['timestamp', 'id', 'created_at', 'updated_at']

    expected = _recursive_remove_keys(expected_json, ignore_keys)
    actual = _recursive_remove_keys(actual_json, ignore_keys)
    assert expected == actual, f"Expected: {expected}, Actual: {actual}"

    return True


def _recursive_remove_keys(json_obj: dict, keys: list) -> dict:
    if not isinstance(json_obj, dict):
        return json_obj

    return {key: _recursive_remove_keys(value, keys) for key, value in json_obj.items() if key not in keys}

    return json_obj


def test_compare_json_objects():
    expected = {
        "name": "John Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zip": 10001
        },
        "timestamp": "2021-01-02T00:00:00Z"
    }

    actual = {
        "name": "John Doe",
        "age": 30,
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "zip": 10001
        },
        "timestamp": "2021-01-01T00:00:00Z"
    }

    assert compare_json_objects(expected, actual)