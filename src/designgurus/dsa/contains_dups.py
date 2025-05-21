
def contains_dups(nums: list[int]) -> bool:
    if not len(set(nums)) == len(nums):
        return True
    return False


if __name__ == '__main__':
    print(contains_dups([1,2,3,4]))
    print(contains_dups([1,2,1,4]))
    print(contains_dups([1,5,3,4]))
