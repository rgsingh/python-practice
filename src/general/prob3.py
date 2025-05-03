"""
Write a Python program that accept an integer test whether an integer is greater than 4^4 and if integer mod 34
is 4
"""


def prob3_integer_size_and_mod(num):
    return (num > 4 ** 4) and 4 == num % 34


if __name__ == '__main__':
    print(prob3_integer_size_and_mod(922))
    print(prob3_integer_size_and_mod(914))
    print(prob3_integer_size_and_mod(854))
