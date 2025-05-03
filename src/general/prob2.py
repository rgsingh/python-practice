"""
Write a Python program that accept a list of integers and check the length and the fifth element. Return true if
the length of the list is 8 and fifth element occurs thrice in the said list.
"""


def prob2_find_match(input_arr):
    return len(input_arr) == 8 and input_arr.count(input_arr[4]) == 3


if __name__ == '__main__':
    print(prob2_find_match([19, 19, 15, 5, 3, 5, 5, 2]))
    print(prob2_find_match([54321, 54321, 15, 19, 54321, 5, 5, 2]))
    print(prob2_find_match([19, 19, 15, 5, 3, 8, 5, 2]))
