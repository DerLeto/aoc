from sys import argv

import numpy as np


def task_1(data_in):
    data = data_in.split(",")
    crabs = np.array(data, dtype=int)

    max_pos = crabs.max()
    min_pos = crabs.min()

    best_cost = 100000000
    best_position = -1
    for destination in range(min_pos, max_pos + 1):
        positions = crabs.copy()
        cost = np.sum(np.abs(positions - destination))

        if cost < best_cost:
            best_cost = cost
            best_position = destination

    return best_cost, best_position



def task_2(data_in):
    data = data_in.split(",")
    crabs = np.array(data, dtype=int)

    max_pos = crabs.max()
    min_pos = crabs.min()

    best_cost = 1000000000000000000000000
    best_position = -1
    for destination in range(min_pos, max_pos + 1):
        positions = crabs.copy()
        cost = np.abs(positions - destination)
        cost = np.sum((cost * (cost + 1)) / 2)

        if cost < best_cost:
            best_cost = cost
            best_position = destination

    return best_cost, best_position


if __name__ == "__main__":
    if len(argv) < 2:
        file = "input.txt"
    else:
        file = argv[1]

    data = open(file)
    cost, position = task_2(data.read())
    print("Cost: " + str(cost) + " | Position: " + str(position))