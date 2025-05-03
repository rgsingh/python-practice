def count_max_frequency(nums):
    default = len(nums) if len(set(nums)) == 1 else 0
    total = default
    num_array = {}
    for num in nums:
        if num in num_array:
            num_array[num] += 1
        else:
            num_array[num] = 1

    sorted_counts = sorted(num_array.values(), reverse=True)
    last_count = None
    for i in range(len(sorted_counts) - 1):
        current_count = sorted_counts[i]
        if last_count is None and last_count != current_count:
            last_count = current_count
        next_count = sorted_counts[i + 1]
        if current_count > next_count and current_count > total:
            total = current_count
        elif current_count == next_count and current_count == last_count and total == default:
            total = current_count + next_count
        elif current_count == next_count and current_count == last_count:
            total += next_count
    return total


if __name__ == '__main__':
    arrays = [
        [],
        [1, 1, 1, 1, 1, 1],
        [3, 2, 2, 3, 1, 4],
        [5, 5, 5, 2, 2, 3],
        [7, 8, 8, 7, 9, 9]
    ]
    for array in arrays:
        print(count_max_frequency(array))
