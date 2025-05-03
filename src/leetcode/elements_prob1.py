def determine_hindex_occurrences(citations: list):
    occurrences = {}
    for citation in citations:
        occurrences[citation] = occurrences.get(citation, 0) + 1

    # if the key of any element of occurrence equals its value plus each value of an element with a key greater than
    # its key, then print out each key
    accumulated_values = {}
    prev_key, prev_value = None, None
    for curr_key, curr_value in occurrences.items():

        if prev_key is not None and prev_key > curr_key:
            continue
        else:
            if curr_value >= curr_key:
                continue
            elif curr_value < curr_key:
                accumulated_values[curr_key] = curr_value

        prev_key, prev_value = curr_key, curr_value

    return accumulated_values


# Step-by-step Execution
# For count = 0
# •	x = 1, 1 >= 0 → yield 1
# •	x = 4, 4 >= 0 → yield 1
# •	x = 1, 1 >= 0 → yield 1
# •	x = 4, 4 >= 0 → yield 1
# •	x = 2, 2 >= 0 → yield 1
# •	x = 1, 1 >= 0 → yield 1
# •	x = 3, 3 >= 0 → yield 1
# •	x = 5, 5 >= 0 → yield 1
# •	x = 6, 6 >= 0 → yield 1
#
# Now we sum up all those yielded 1s:
#
#
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 9
#
def h_index(citations):
    count = 0
    while sum(1 for x in citations if x >= count) >= count:
        count += 1
    return count - 1


if __name__ == '__main__':
    print(h_index([1, 4, 1, 4, 2, 1, 3, 5, 6]))

    print(h_index([5, 3, 6, 3, 7, 2, 7, 1, 6]))
