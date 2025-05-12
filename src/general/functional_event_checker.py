def check_has_field(field: str):
    def check(event):
        return field in event
    return check


if __name__ == '__main__':
    event_payload = {"type": "login", "user": "bob", "timestamp": 123456}
    required_fields = ["type", "timestamp"]

    has_type = check_has_field("type")
    print(has_type(event_payload))

    has_session_id = check_has_field("session_id")
    print(has_session_id(event_payload))

