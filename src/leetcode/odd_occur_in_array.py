
def odd_occurrence(arr):
    result = 0
    for num in arr:
        result ^= num
    return result

if __name__ == '__main__':
    print(odd_occurrence([9, 7, 9, 3, 9, 3, 9]))  # Output: 7