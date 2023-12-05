import math
from sys import argv

import numpy as np

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
closing = [')', ']', '}', '>']
opening = ['(', '[', '{', '<']

scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
scores2 = {')': 1, ']': 2, '}': 3, '>': 4}

def task_1(data_in):
    data = data_in.split('\n')

    score = 0
    for line in data:
        basement = []
        for char in line:
            if char in opening:
                basement.append(char)
            elif char in closing:
                openChar = basement.pop()
                if char != pairs[openChar]:
                    score += scores[char]

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