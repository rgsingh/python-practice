"""Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct."""


# Without set
def contains_dups2(nums) -> bool:
    at_least_once = []
    for num in nums:
        if num in at_least_once:
            return True
        else:
            at_least_once.append(num)
    return False


def contains_dups3(nums) -> bool:
    seen = []

    for n in nums:
        if n in seen:
            return True
        else:
            seen.append(n)
    return False


def contains_dups(nums) -> bool:
    return len(set(nums)) < len(nums)


if __name__ == '__main__':
    print(contains_dups3([1, 2, 3, 4]))
    print(contains_dups3([1, 2, 1, 4]))
    print(contains_dups3([1, 2, 1, 4, 3, 1, 5, 4, 6, 8, 2]))
    print(contains_dups3([8, 6, 7, 5, 3, 1, 9]))
