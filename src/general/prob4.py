"""
We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of
stones. If n is odd, all piles have an odd number of stones. Each pile must have more stones than the previous pile but
as few as possible. Write a Python program to find the number of stones in each pile and the total of all piles
in a sequence of piles.
"""


def prob4_make_piles_of_stones(num_piles):
    output = [0] * num_piles
    i = 0
    while i < num_piles:
        output[i] = output[i - 1] + 2 if i > 0 else num_piles
        i += 1
    return output, sum(output)


if __name__ == '__main__':
    print(prob4_make_piles_of_stones(2))
    print(prob4_make_piles_of_stones(10))
    print(prob4_make_piles_of_stones(3))
    print(prob4_make_piles_of_stones(17))
