"""Imagine you’re a gem collector. You have a bag of random stones, and a short list of what you consider jewels.
You want to know how many of the stones in your bag are actually jewels."""

# No added build cost for string scan (spacial time) but slower lookup due to string scan - O(n x m) time, O(1) space
def num_of_jewel_stones(jewels: str, stones: str) -> int:
    count_jewels = 0
    for stone in stones:
        if stone in jewels:
            count_jewels += 1
    return count_jewels

# Addition build cost (spacial time) for set but faster lookup due to use set usage - O(n + m) time, O(m) space
def num_of_jewel_stones2(jewels: str, stones: str) -> int:
    jewel_set = set(jewels)
    return sum(stone in jewel_set for stone in stones)

if __name__ == '__main__':
    print(num_of_jewel_stones("aA", "aAAbbbb"))
    print(num_of_jewel_stones("fjA21", "hJjB71102"))

    print(num_of_jewel_stones2("aA", "aAAbbbb"))
    print(num_of_jewel_stones2("fjA21", "hJjB71102"))
