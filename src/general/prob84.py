"""A string is happy if every 3 consecutive characters are distinct . Write a program to find the 2 indices
making a given string unhappy :("""


def seek_the_unhappy(input_string):
    unhappy_ones = []
    for position in range(0, len(input_string) - 1, 3):
        for inner_pos in range(position + 1, position + 3):
            if input_string[position] == input_string[inner_pos]:
                unhappy_ones.append([inner_pos, input_string[inner_pos]])

    return unhappy_ones


if __name__ == '__main__':
    print(seek_the_unhappy("abcdefeghhehxyzdgd"))
