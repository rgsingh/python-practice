from general.constants import COERCION_RULES


def coerce_unnested_payload(payload: dict, schema: dict):
    coerced = {}

    for key, expected_type in schema.items():
        value = payload.get(key)

        actual_type = type(value)

        if actual_type == expected_type:
            coerced[key] = value
        elif actual_type in COERCION_RULES.get(expected_type, []):
            try:
                coerced[key] = expected_type(value)
            except Exception as e:
                ValueError(f"Cannot coerce {key} with actual type {actual_type} to {expected_type}: {e}")
        else:
            raise TypeError(f"Unsupported coercion from {actual_type} to {expected_type} for {value}")

    return coerced


example_payload = {
    "user_id": "42",
    "is_active": "true",
    "score": "99.5"
}

example_schema = {
    "user_id": int,
    "is_active": bool,
    "score": float
}

if __name__ == "__main__":
    coerced = coerce_unnested_payload(example_payload, example_schema)
    print("Coerced Result:", coerced)
