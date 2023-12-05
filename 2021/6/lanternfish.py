from sys import argv

import numpy as np
from psutil import long


def task_1(data_in, days):
    data = data_in.split(',')
    fish = np.asarray(data, dtype=int)
    print(fish)

    for i in range(days):
        print(i)
        number_new_fish = (fish == 0).sum()
        fish[fish == 0] = 7
        fish = np.append(fish, 9 * np.ones(number_new_fish, dtype=int))
        fish -= 1

    print(fish)

    return fish.shape[0]


def task_2(data_in, days):
    data = [int(x) for x in data_in.split(',')]
    fish = np.asarray([data.count(x) for x in range(9)], dtype=np.longlong)
    print(fish)

    for i in range(days):
        print(i)
        new_fish = fish[0]
        fish[7] += fish[0]

        for i in range(8):
            fish[i] = fish[i+1]

        fish[8] = new_fish
        print(fish)

    print(fish)

    return fish.sum()


if __name__ == "__main__":
    if len(argv) < 2:
        file = "input.txt"
    else:
        file = argv[1]

    data = open(file)
    days = 256  # 80: 374994
    number = task_2(data.read(), days)
    print("Result: " + str(number))