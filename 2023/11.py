import numpy as np

input_path = "input/11.txt"


def expand(grid: np.array):
    X, Y = grid.shape
    sums = np.sum(grid, axis=1)

    indeces_x = []
    indeces_y = []

    x = 0
    for sum in sums:
        if sum == 0:
            indeces_x.append(x)
        x += 1

    X, Y = grid.shape
    sums = np.sum(grid, axis=0)
    y = 0
    for sum in sums:
        if sum == 0:
            indeces_y.append(y)
        y += 1

    return indeces_x, indeces_y


def find_galaxies(grid):
    indeces = np.where(grid > 0)
    return [(x, y) for x, y in zip(indeces[0], indeces[1])]


def bfs(grid, start, end):
    X, Y = grid.shape
    visited = [start]
    Q = [start]

    print(str(start) + " - " + str(end))
    depth = 0
    while len(Q) > 0:
        new_Q = []
        for node in Q:
            if node == end:
                return depth

            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    x = node[0] + dx
                    y = node[1] + dy

                    if (x, y) in visited:
                        continue

                    if not dx == 0 and not dy == 0:
                        continue

                    if abs(end[0] - node[0]) < abs(end[0] - x):
                        continue

                    if abs(end[1] - node[1]) < abs(end[1] - y):
                        continue

                    if 0 <= x < X and 0 <= y < Y:
                        new_Q.append((x, y))
                        visited.append((x, y))
        Q = new_Q
        depth += 1

    raise Exception("Impossible")


def a():
    with open(input_path) as file:
        data = file.read().strip().split("\n")

    grid = np.zeros(shape=(len(data), len(data[0])))
    counter = 1
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == "#":
                grid[x, y] = counter
                counter += 1

    print(grid)
    indeces_x, indeces_y = expand(grid)
    galaxies = find_galaxies(grid)
    print(galaxies)

    res = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            start = galaxies[i]
            end = galaxies[j]
            shortest_path = abs(end[0] - start[0]) + abs(end[1] - start[1])

            for x in indeces_x:
                if min(start[0], end[0]) < x < max(start[0], end[0]):
                    shortest_path += 1

            for y in indeces_y:
                if min(start[1], end[1]) < y < max(start[1], end[1]):
                    shortest_path += 1

            res += shortest_path

    return res


def b():
    with open(input_path) as file:
        data = file.read().strip().split("\n")

    grid = np.zeros(shape=(len(data), len(data[0])))
    counter = 1
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == "#":
                grid[x, y] = counter
                counter += 1

    print(grid)
    indeces_x, indeces_y = expand(grid)
    galaxies = find_galaxies(grid)
    print(galaxies)

    res = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            start = galaxies[i]
            end = galaxies[j]
            shortest_path = abs(end[0] - start[0]) + abs(end[1] - start[1])

            for x in indeces_x:
                if min(start[0], end[0]) < x < max(start[0], end[0]):
                    shortest_path += 1000000 - 1

            for y in indeces_y:
                if min(start[1], end[1]) < y < max(start[1], end[1]):
                    shortest_path += 1000000 - 1

            res += shortest_path

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
