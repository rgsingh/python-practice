

def reverse_digits(num: int) -> int:
    str_num = str(num)
    max_idx = len(str_num) - 1
    str_reversed = [0] * len(str_num)

    for idx, char in enumerate(str_num):
        str_reversed[max_idx] = char
        max_idx = max_idx - 1

    return int("".join(map(str, str_reversed)))


def reverse_digits_math(num: int) -> int:
    res = 0
    is_negative = num < 0
    num = abs(num)

    while num > 0:
        res = res * 10 + num % 10
        num //= 10

    return -res if is_negative else res


if __name__ == '__main__':
    # print(reverse_digits(324))

    print(reverse_digits_math(324))
