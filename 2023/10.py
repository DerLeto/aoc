import math

input_path = "input/10.txt"

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.


indeces = []


def find_start(grid):
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char == "S":
                return x, y


def find_first(grid, start):
    x, y = start
    if grid[x + 1][y] in ["|", "J", "L"]:
        return x + 1, y
    elif grid[x - 1][y] in ["|", "7", "F"]:
        return x - 1, y
    elif grid[x][y + 1] in ["-", "7", "J"]:
        return x, y + 1
    elif grid[x][y - 1] in ["-", "L", "F"]:
        return x, y - 1


def bfs(grid, start, first):
    last = start
    current = first
    depth = 0
    while True:
        if current in indeces:
            print("REPEAT")
        else:
            indeces.append(current)

        x, y = current
        symbol = grid[x][y]
        node = None
        if symbol == "S":
            return depth
        elif symbol == "|":
            if not (x - 1, y) == last:
                node = (x - 1, y)
            else:
                node = (x + 1, y)
        elif symbol == "-":
            if not (x, y - 1) == last:
                node = (x, y - 1)
            else:
                node = (x, y + 1)
        elif symbol == "L":
            if not (x - 1, y) == last:
                node = (x - 1, y)
            else:
                node = (x, y + 1)
        elif symbol == "J":
            if not (x - 1, y) == last:
                node = (x - 1, y)
            else:
                node = (x, y - 1)
        elif symbol == "7":
            if not (x + 1, y) == last:
                node = (x + 1, y)
            else:
                node = (x, y - 1)
        elif symbol == "F":
            if not (x, y + 1) == last:
                node = (x, y + 1)
            else:
                node = (x + 1, y)

        # print(str(grid[node[0]][node[1]]) + ": " + str(node))
        last = current
        current = node
        depth += 1


def a():
    res = 0
    grid = []
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            row = []
            for char in line_stripped:
                row.append(char)
            grid.append(row)

    start = find_start(grid)
    first = find_first(grid, start)
    res = math.ceil(0.5 * bfs(grid, start, first))

    return res


def b():
    res = 0
    grid = []
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            row = []
            for char in line_stripped:
                row.append(char)
            grid.append(row)

    start = find_start(grid)
    first = find_first(grid, start)
    print(start)
    print(str(grid[first[0]][first[1]]) + ": " + str(first))
    res = math.ceil(0.5 * bfs(grid, start, first))

    res = 0
    print(indeces)

    for x, row in enumerate(grid):
        inside = False
        for y, char in enumerate(row):
            if char in ["|", "L", "J", "S"] and (x, y) in indeces:
                inside = not inside
            elif inside and (x, y) not in indeces:
                print(x, y)
                res += 1
    return res


def print_array(array):
    with open("./input/10.map", "w+") as file:
        for row in array:
            for char in row:
                file.write(str(char))
            file.write("\n")


def main():
    # res_a = a()
    res_b = b()
    # print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
