def count_each_char_occurrences(input_str, pattern):
    """
    Count the number of occurrences of each character in the input string
    :param input_str: input string
    :param pattern: pattern to match
    :return: dictionary of character and its count
    """
    char_count = {}
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count.get(pattern, 0)


def count_all_occurrences(input_str):
    char_counts = {}
    for char in input_str:
        if char in char_counts.keys():
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


if __name__ == '__main__':
    print(count_each_char_occurrences("hello", "l"))
    print(count_each_char_occurrences("hello", "o"))
    print(count_each_char_occurrences("hello", "z"))
    print(count_each_char_occurrences("hello", "h"))
    print(count_each_char_occurrences("hello", "e"))

    occurrence_object = count_all_occurrences("hello")
    print(occurrence_object)

    sorted_occurrences = []
    print(sorted(occurrence_object.items(), key=lambda item: item[1], reverse=True))

    sorted_values = sorted(occurrence_object.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_values:
        print(f'{key}:{value}')