

def running_sum(nums: list[int]):
    result = [0] * len(nums)
    for idx, num in enumerate(nums):
        result[idx] = num + result[idx-1]
    return result



if __name__ == '__main__':
    print(running_sum([3,1,4,2,2]))