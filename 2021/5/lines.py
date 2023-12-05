from sys import argv

import numpy as np


def task_1(data_in):
    data = data_in.split('\n')
    field = np.zeros((1000, 1000))

    for line in data:
        start, end = line.split(' -> ')
        x1, y1 = [int(number) for number in start.split(',')]
        x2, y2 = [int(number) for number in end.split(',')]

        if x1 == x2:
            if y1 > y2:
                field[x1, y2:y1+1] += 1
            else:
                field[x1, y1:y2+1] += 1
        elif y1 == y2:
            if x1 > x2:
                field[x2:x1+1, y1] += 1
            else:
                field[x1:x2+1, y1] += 1

    print(field)

    return (field >= 2).sum()


def task_2(data_in):
    data = data_in.split('\n')
    field = np.zeros((1000, 1000))

    for line in data:
        start, end = line.split(' -> ')
        x1, y1 = [int(number) for number in start.split(',')]
        x2, y2 = [int(number) for number in end.split(',')]

        if x1 == x2:
            if y1 > y2:
                field[x1, y2:y1 + 1] += 1
            else:
                field[x1, y1:y2 + 1] += 1
        elif y1 == y2:
            if x1 > x2:
                field[x2:x1 + 1, y1] += 1
            else:
                field[x1:x2 + 1, y1] += 1
        else:
            if x1 > x2 and y1 > y2:
                for i in range(0, x1-x2+1):
                    field[x1-i, y1-i] += 1
            elif x1 > x2 and y1 < y2:
                for i in range(0, x1-x2+1):
                    field[x1-i, y1+i] += 1
            elif x1 < x2 and y1 < y2:
                for i in range(0, x2-x1+1):
                    field[x2-i, y2-i] += 1
            else:
                for i in range(0, x2 - x1 + 1):
                    field[x2 - i, y2 + i] += 1

    print(field)

    return (field >= 2).sum()


if __name__ == "__main__":
    if len(argv) < 2:
        file = "input.txt"
    else:
        file = argv[1]

    data = open(file)
    number = task_2(data.read())
    print("Result: " + str(number))