"""Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings."""


def valid_string_in_which(position, input_arr):
    matched_against = []
    i = 0
    if position >= len(input_arr):
        raise Exception('zero-based position must be within bounds of input_arr')

    while len(input_arr) - 1 > i >= 0:
        if input_arr[position] in input_arr[i+1] and (position != i+1):
            matched_against.append(input_arr[i+1])
        i += 1

    return len(matched_against) > 0, matched_against


if __name__ == '__main__':
    print(valid_string_in_which(0, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
    print(valid_string_in_which(4, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
    print(valid_string_in_which(3, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
    print(valid_string_in_which(-1, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
    print(valid_string_in_which(-3, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))
    print(valid_string_in_which(6, ['a', 'abb', 'sfs', 'oo', 'de', 'sfde']))

