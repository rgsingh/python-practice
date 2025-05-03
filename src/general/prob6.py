"""Write a Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one
another. Return true or false """
import numpy as np


def apart_by_ten(input_arr):
    status = False

    reversed_array = np.sort(input_arr)[::-1]
    if reversed_array[0] > 990:
        raise Exception('Illegal value exceeds maximum', reversed_array[0])

    for i in range(len(input_arr)):
        current_adjusted_val = input_arr[i] + 10
        if i != len(input_arr) - 1 and current_adjusted_val != input_arr[i + 1]:
            status = False
            break
        else:
            status = True

    return status


if __name__ == '__main__':
    print(apart_by_ten([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150,
                        160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290,
                        300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430,
                        440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570,
                        580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710,
                        720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850,
                        860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990]))
