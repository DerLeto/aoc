import numpy as np

input_path = "input/14.txt"

def parse_grid():
    with open(input_path) as file:
        data = file.read().strip().split("\n")

    X = len(data)
    Y = len(data[0])

    grid = np.zeros(shape=(X, Y))
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            if char == "#":
                grid[x, y] = 1
            elif char == "O":
                grid[x, y] = 2

    return grid


def tilt(grid, dir):
    X, Y = grid.shape

    if dir == 0:
        for y in range(Y):
            last_cube = -1
            for x in range(X):
                value = grid[x, y]
                if value == 1:
                    last_cube = x
                elif value == 2:
                    last_cube += 1
                    grid[x, y] = 0
                    grid[last_cube, y] = 2
    elif dir == 1:
        for x in range(X):
            last_cube = -1
            for y in range(Y):
                value = grid[x, y]
                if value == 1:
                    last_cube = y
                elif value == 2:
                    last_cube += 1
                    grid[x, y] = 0
                    grid[x, last_cube] = 2
    elif dir == 2:
        for y in range(Y):
            last_cube = X
            for x in range(X - 1, -1, -1):
                value = grid[x, y]
                if value == 1:
                    last_cube = x
                elif value == 2:
                    last_cube -= 1
                    grid[x, y] = 0
                    grid[last_cube, y] = 2
    elif dir == 3:
        for x in range(X):
            last_cube = Y
            for y in range(Y - 1, -1, -1):
                value = grid[x, y]
                if value == 1:
                    last_cube = y
                elif value == 2:
                    last_cube -= 1
                    grid[x, y] = 0
                    grid[x, last_cube] = 2
    else:
        raise Exception

    return grid


def calculate_points(grid):
    res = 0
    X, Y = grid.shape
    points = Y
    for x in range(X):
        for y in range(Y):
            value = grid[x, y]
            if value == 2:
                res += points
        points -= 1
    return res


def a():
    res = 0
    grid = parse_grid()
    grid = tilt(grid, 0)
    res = calculate_points(grid)

    return res


def b():
    res = 0
    grid = parse_grid()
    print(grid)

    beginning = 110
    cycle = 9
    #beginning = 3
    #cycle = 7
    for i in range(int(((1000000000 - beginning) % cycle)) + beginning):
        #print(i)
        for j in range(4):
            grid = tilt(grid, j)
        res = calculate_points(grid)
        print(f"{i + 1}: {res}")



    return res


def main():
    #res_a = a()
    res_b = b()
    #print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
