"""Write a Python program to check the string at position is a proper substring
of any string in a given list of strings. Return a both True/False and the matching occurrences"""


def valid_string_in_which(position, input_arr):
    matched_against = []
    i = 0
    if not -len(input_arr) <= position < len(input_arr):
        # raise Exception('zero-based position must be within bounds of input_arr')
        return "UNRESOLVABLE_SUBSTR", False, "UNRESOLVABLE_TARGET"

    target_str = input_arr[position]

    for idx, s in enumerate(input_arr):
        if idx != position and target_str in s:
            matched_against.append(s)

    return input_arr[position], len(matched_against) > 0, matched_against


if __name__ == '__main__':
    print(valid_string_in_which(0, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
    print(valid_string_in_which(4, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
    print(valid_string_in_which(3, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
    print(valid_string_in_which(-1, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
    print(valid_string_in_which(-3, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
    print(valid_string_in_which(6, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))

