
def find_longest_gap(input: int) -> int:
    binary_num = bin(input)
    counting = False
    current_gap = 0
    max_gap = 0

    for digit in binary_num:
        if digit == "1":
            if counting:
                max_gap = max(max_gap, current_gap)
            counting = True
            current_gap = 0
        elif counting:
            current_gap += 1

    return max_gap


if __name__ == '__main__':
    print(find_longest_gap(529))  # 4
    print(find_longest_gap(20))   # 1
    print(find_longest_gap(15))   # 0
    print(find_longest_gap(1041)) # 5