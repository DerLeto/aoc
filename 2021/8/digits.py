import math
from sys import argv

import numpy as np

relation = ['a', 'b', 'c', 'd', 'e', 'f', 'g']


def task_1(data_in):
    lines = data_in.split("\n")
    count = 0
    for line in lines:
        data = line.split(" | ")[-1]
        numbers = data.split(" ")
        for number in numbers:
            if len(number) in [2, 3, 4, 7]:
                count += 1

    return count


def task_2(data_in):
    # 1 and 7 -> a
    # a -> 8
    # b -> 6
    # c -> 8
    # d -> 7 and in 4
    # e -> 4
    # f -> 9
    # g -> 7 and not in 4
    lines = data_in.split("\n")
    overall_sum = 0
    for line in lines:
        data = line.split(" | ")[0]
        result = line.split(" | ")[-1]
        numbers = data.split(" ")

        # find mapping
        count = [0, 0, 0, 0, 0, 0, 0]
        one = ""
        four = ""
        for number in numbers:
            if len(number) == 2:
                one = number
            elif len(number) == 4:
                four = number
            for char in number:
                count[ord(char) - 97] += 1

        for i in range(7):
            entry = count[i]
            if entry == 8 and chr(i + 97) not in one:
                relation[0] = chr(i + 97)
            elif entry == 6:
                relation[1] = chr(i + 97)
            elif entry == 8:
                relation[2] = chr(i + 97)
            elif entry == 7 and chr(i + 97) in four:
                relation[3] = chr(i + 97)
            elif entry == 4:
                relation[4] = chr(i + 97)
            elif entry == 9:
                relation[5] = chr(i + 97)
            elif entry == 7:
                relation[6] = chr(i + 97)

        # get number
        numbers = result.split(" ")
        number = 0
        for i in range(4):
            code = numbers[3-i]
            digit = None
            if len(code) == 2:
                digit = 1
            elif len(code) == 3:
                digit = 7
            elif len(code) == 4:
                digit = 4
            elif len(code) == 7:
                digit = 8
            elif len(code) == 6 and relation[3] not in code:
                digit = 0
            elif len(code) == 6 and relation[2] not in code:
                digit = 6
            elif len(code) == 6:
                digit = 9
            elif relation[2] in code and relation[4] in code:
                digit = 2
            elif relation[2] in code:
                digit = 3
            else:
                digit = 5

            number += digit * 10**i

        overall_sum += number

    return overall_sum


if __name__ == "__main__":
    if len(argv) < 2:
        file = "input.txt"
    else:
        file = argv[1]

    data = open(file)
    count = task_2(data.read())
    print("Count: " + str(count))
