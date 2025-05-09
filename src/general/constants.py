import datetime

COERCION_RULES = {
    datetime.datetime: [str],
    int: [str, float],
    float: [str, int],
    bool: [str, int],
    str: [int, float, bool, datetime.datetime]
}
