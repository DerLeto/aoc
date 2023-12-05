import math
import sys
from sys import argv

import numpy as np

np.set_printoptions(threshold=sys.maxsize)

lenX = 0
lenY = 0

def task_1(data_in):
    lines = data_in.split("\n")
    heightmap = []
    for line in lines:
        data = []
        for number in line:
            data.append(int(number))
        heightmap.append(data)

    minPoints = np.zeros((len(heightmap), len(heightmap[0])), dtype=int)
    for x in range(len(heightmap)):
        for y in range(len(heightmap[0])):
            height = heightmap[x][y]
            if x > 0 and heightmap[x-1][y] <= height:
                continue
            elif x < len(heightmap) - 1 and heightmap[x+1][y] <= height:
                continue
            elif y > 0 and heightmap[x][y-1] <= height:
                continue
            elif y < len(heightmap[0]) - 1 and heightmap[x][y+1] <= height:
                continue
            else:
                minPoints[x, y] = height + 1

    return np.sum(minPoints)


def task_2(data_in):
    lines = data_in.split("\n")
    heightmap = []
    for line in lines:
        data = []
        for number in line:
            data.append(int(number))
        heightmap.append(data)

    #minPoints = np.zeros((len(heightmap), len(heightmap[0])), dtype=int)
    minPoints = []
    global lenX
    global lenY
    lenX = len(heightmap)
    lenY = len(heightmap[0])
    for x in range(len(heightmap)):
        for y in range(len(heightmap[0])):
            height = heightmap[x][y]
            if x > 0 and heightmap[x - 1][y] <= height:
                continue
            elif x < len(heightmap) - 1 and heightmap[x + 1][y] <= height:
                continue
            elif y > 0 and heightmap[x][y - 1] <= height:
                continue
            elif y < len(heightmap[0]) - 1 and heightmap[x][y + 1] <= height:
                continue
            else:
                #minPoints[x, y] = height + 1
                minPoints.append((x, y))

    print(minPoints)

    basinsCount = []
    for x, y in minPoints:
        visitedIndeces = []
        count = move(x, y, visitedIndeces, heightmap)
        basinsCount.append(count)

    print(basinsCount)

    first = 0
    second = 0
    third = 0
    for count in basinsCount:
        if count > first:
            third = second
            second = first
            first = count
        elif count > second:
            third = second
            second = count
        elif count > third:
            third = count

    return first*second*third

def move(x, y, visitedIndeces, heightmap):
    if heightmap[x][y] == 9:
        return 0

    if (x, y) in visitedIndeces:
        return 0
    else:
        visitedIndeces.append((x, y))

    count = 1
    if x > 0:
        count += move(x-1, y, visitedIndeces, heightmap)
    if x < lenX - 1:
        count += move(x + 1, y, visitedIndeces, heightmap)
    if y > 0:
        count += move(x, y-1, visitedIndeces, heightmap)
    if y < lenY - 1:
        count += move(x, y+1, visitedIndeces, heightmap)

    return count



if __name__ == "__main__":
    if len(argv) < 2:
        file = "input.txt"
    else:
        file = argv[1]

    data = open(file)
    level = task_2(data.read())
    print("Level: " + str(level))