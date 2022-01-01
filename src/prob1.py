"""
Write a Python program find a list of integers with exactly two occurrences of nineteen and at least three
occurrences of five.
"""


def prob1_find_match(input_arr):
    return input_arr.count(19) == 2 and input_arr.count(5) >= 3


if __name__ == '__main__':
    print(prob1_find_match([19, 19, 15, 5, 3, 5, 5, 2]))
    print(prob1_find_match([19, 19, 15, 19, 3, 5, 5, 2]))
    print(prob1_find_match([19, 19, 15, 5, 3, 8, 5, 2]))
