import numpy as np

input_path = "input/13.txt"

def handle_pattern_a(pattern):
    res = 0
    data = pattern.strip().split("\n")
    X = len(data)
    Y = len(data[0])

    grid = np.zeros(shape=(X, Y))
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == "#":
                grid[x, y] = 1

    print(grid)
    for x in range(X - 1):
        if all(grid[x] == grid[x + 1]):
            all_ok = True
            distance = min(x, X - (x + 1) - 1)
            for xx in range(1, distance + 1):
                if not all(grid[x - xx] == grid[x + 1 + xx]):
                    all_ok = False
                    break

            if all_ok:
                res += (x + 1) * 100

    for x in range(Y - 1):
        if all(grid[:, x] == grid[:, x + 1]):
            all_ok = True
            distance = min(x, Y - (x + 1) - 1)
            for xx in range(1, distance + 1):
                if not all(grid[:, x - xx] == grid[:, x + 1 + xx]):
                    all_ok = False
                    break

            if all_ok:
                res += (x + 1)

    return res

def a():
    res = 0
    with open(input_path) as file:
        data = file.read().strip()

    for pattern in data.split("\n\n"):
        res += handle_pattern_a(pattern)

    return res


def handle_pattern_b(pattern):
    res = 0
    data = pattern.strip().split("\n")
    X = len(data)
    Y = len(data[0])

    grid = np.zeros(shape=(X, Y))
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == "#":
                grid[x, y] = 1

    print(grid)
    for x in range(X - 1):
        joker = 1
        all_ok = True
        distance = min(x, X - (x + 1) - 1)
        for xx in range(0, distance + 1):
            for y in range(Y):
                if grid[x - xx, y] != grid[x + 1 + xx, y]:
                    if joker > 0:
                        joker -= 1
                    else:
                        all_ok = False
                        break
        if all_ok and joker == 0:
            res += (x + 1) * 100

    for y in range(Y - 1):
        joker = 1
        all_ok = True
        distance = min(y, Y - (y + 1) - 1)
        for yy in range(0, distance + 1):
            for x in range(X):
                if grid[x, y - yy] != grid[x, y + 1 + yy]:
                    if joker > 0:
                        joker -= 1
                    else:
                        all_ok = False
                        break
        if all_ok and joker == 0:
            res += (y + 1)

    return res


def b():
    res = 0
    with open(input_path) as file:
        data = file.read().strip()

    for pattern in data.split("\n\n"):
        res += handle_pattern_b(pattern)

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
