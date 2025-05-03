import time


def binary_search(input_array, x):
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low + high) // 2
        if input_array[mid] < x:
            low = mid + 1
        elif input_array[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    # unsorted array
    arr = [2, 3, 4, 10, 40]

    start_time = time.perf_counter()
    print(binary_search(arr, 10))
    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1e6

    print(f"Time taken: {elapsed_time} microseconds")
