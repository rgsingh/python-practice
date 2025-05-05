"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""


def two_sum2(nums: list[int], target: int) -> dict:
    seen = {}
    matched_tuple = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            matched_tuple = (nums.index(diff), nums.index(num))
            break
        seen[num] = True
    return matched_tuple


def two_sum(nums, target):
    seen = {}
    for num in nums:
        diff = target - num
        if diff in seen:
            print(diff, num)
            break
        seen[num] = True


if __name__ == '__main__':
    input_nums = [2, 7, 11, 15]
    input_target = 9
    match = two_sum2(input_nums, input_target)
    print(match)

    input_nums = [15, 12, 8, 2]
    input_target = 14
    match = two_sum2(input_nums, input_target)
    print(match)
