from datetime import datetime

from general.constants import COERCION_RULES

def _try_coerce_datetime(value: str) -> datetime:
    try:
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ")
    except ValueError:
        raise ValueError(f"Unable to coerce {value} from str to datetime")



def coerce_type(payload: dict, schema: dict, path="root") -> dict:
    coerced = {}

    for key, expected_type in schema.items():
        current_path = f"{path}.{key}"
        value = payload.get(key, "")
        actual_type = type(value)

        if isinstance(value, dict):
            coerced[key] = coerce_type(value, expected_type, current_path)
        else:
            if actual_type == expected_type:
                coerced[key] = value
            elif actual_type in COERCION_RULES.get(expected_type, []):
                try:
                    if expected_type == datetime:
                        coerced[key] = _try_coerce_datetime(value)
                    else:
                        coerced[key] = expected_type(value)
                except Exception as e:
                    raise ValueError(f"Invalid type coercion from {actual_type} tp {expected_type} for {key}")
            else:
                raise TypeError(f"Unsupported type coercion from {actual_type} tp {expected_type} for {key}")

    return coerced


if __name__ == '__main__':
    input_payload = {
        "applicationId": "06bd6ecf-8b74-450e-bd5d-3a0439d4a80e",
        "isActive": "false",
        "metadata": {
            "owner": "fulfillment",
        },
        "event_time": "2025-05-09T20:37:42Z"
    }

    schema_definition = {
        "applicationId": str,
        "isActive": bool,
        "metadata": {
            "owner": str,
        },
        "event_time": datetime
    }

    print(coerce_type(input_payload, schema_definition))
