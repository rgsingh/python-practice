def count_max_frequency(nums):
    # Dictionary to store frequency of elements
    frequency_map = {}

    # Calculate the frequency of each element
    for num in nums:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1

    # Find the maximum frequency
    max_frequency = max(frequency_map.values())

    # Sum the frequencies of elements with maximum frequency
    total_max_frequency = sum(frequency for frequency in frequency_map.values() if frequency == max_frequency)

    return total_max_frequency


if __name__ == "__main__":

    nums0 = [1, 1, 1, 1, 1, 1]
    print(count_max_frequency(nums0))

    # Test example 1
    nums1 = [3, 2, 2, 3, 1, 4]
    print(count_max_frequency(nums1))  # Output: 4

    # Test example 2
    nums2 = [5, 5, 5, 2, 2, 3]
    print(count_max_frequency(nums2))  # Output: 3

    # Test example 3
    nums3 = [7, 8, 8, 7, 9, 9]
    print(count_max_frequency(nums3))  # Output: 6
