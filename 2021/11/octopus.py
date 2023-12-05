import math
from sys import argv

import numpy as np

def task_1(data_in):
    lines = data_in.split('\n')
    octopuses = np.zeros((10, 10))
    for i in range(10):
        for j in range(10):
            octopuses[i, j] = lines[i, j]

    for i in range(100):
        octopuses += 1

    return score

def task_2(data_in):
    data = data_in.split('\n')

    totalScores = []
    for line in data:
        basement = []
        corrupted = False
        for char in line:
            if char in opening:
                basement.append(char)
            elif char in closing:
                openChar = basement.pop()
                if char != pairs[openChar]:
                    corrupted = True

        if not corrupted:
            basement.reverse()
            remaining = ""
            score = 0
            for open in basement:
                remaining += pairs[open]
                score *= 5
                score += scores2[pairs[open]]

            totalScores.append(score)

    totalScores.sort()

    return totalScores[math.floor(len(totalScores)/2)]


if __name__ == "__main__":
    if len(argv) < 2:
        file = "input.txt"
    else:
        file = argv[1]

    data = open(file)
    score = task_2(data.read())
    print("Score: " + str(score))