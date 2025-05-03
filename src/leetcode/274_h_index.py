# For count = 0
# •	x = 3, 3 >= 0 → yield 1
# •	x = 5, 5 >= 0 → yield 1
# •	x = 2, 2 >= 0 → yield 1
# •	x = 3, 3 >= 0 → yield 1
# •	x = 5, 5 >= 0 → yield 1
# •	x = 7, 7 >= 0 → yield 1
# •	x = 8, 8 >= 0 → yield 1
# •	x = 3, 3 >= 0 → yield 1
# •	x = 1, 1 >= 0 → yield 1
# •	x = 4, 4 >= 0 → yield 1
#
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10
#

# For count = 1
# •	x = 3, 3 >= 1 → yield 1
# •	x = 5, 5 >= 1 → yield 1
# •	x = 2, 2 >= 1 → yield 1
# •	x = 3, 3 >= 1 → yield 1
# •	x = 5, 5 >= 1 → yield 1
# •	x = 7, 7 >= 1 → yield 1
# •	x = 8, 8 >= 1 → yield 1
# •	x = 3, 3 >= 1 → yield 1
# •	x = 1, 1 >= 1 → yield 1
# •	x = 4, 4 >= 1 → yield 1
#
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10
#

# For count = 2
# •	x = 3, 3 >= 2 → yield 1
# •	x = 5, 5 >= 2 → yield 1
# •	x = 2, 2 >= 2 → yield 1
# •	x = 3, 3 >= 2 → yield 1
# •	x = 5, 5 >= 2 → yield 1
# •	x = 7, 7 >= 2 → yield 1
# •	x = 8, 8 >= 2 → yield 1
# •	x = 3, 3 >= 2 → yield 1
# •	x = 4, 4 >= 2 → yield 1
#
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1  = 9
#


# For count = 3
# •	x = 3, 3 >= 3 → yield 1
# •	x = 5, 5 >= 3 → yield 1
# •	x = 3, 3 >= 3 → yield 1
# •	x = 5, 5 >= 3 → yield 1
# •	x = 7, 7 >= 3 → yield 1
# •	x = 8, 8 >= 3 → yield 1
# •	x = 3, 3 >= 3 → yield 1
# •	x = 4, 4 >= 3 → yield 1
#
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1  = 8
#
# For count = 4 <==== h-index 4 which corresponds to 5 different papers that have each been published at least 4 times
# •	x = 5, 5 >= 4 → yield 1
# •	x = 5, 5 >= 4 → yield 1
# •	x = 7, 7 >= 4 → yield 1
# •	x = 8, 8 >= 4 → yield 1
# •	x = 4, 4 >= 4 → yield 1
#
# 1 + 1 + 1 + 1 + 1 = 5
#

# For count = 5
# •	x = 5, 5 >= 5 → yield 1
# •	x = 5, 5 >= 5 → yield 1
# •	x = 7, 7 >= 5 → yield 1
# •	x = 8, 8 >= 5 → yield 1
#
# 1 + 1 + 1 + 1 = 4
#
def h_index(citations):
    count = 0
    while sum(1 for x in citations if x >= count) >= count:
        count += 1
    return count - 1


if __name__ == '__main__':
    input_citations = [3, 5, 2, 3, 5, 7, 8, 3, 1, 4]

    print(h_index(input_citations))
