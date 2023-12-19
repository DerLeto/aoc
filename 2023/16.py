input_path = "input/16.txt"


def parse_input():
    grid = []
    with open(input_path) as file:
        for line in file:
            row = []
            grid.append(row)
            line_stripped = line.strip()
            for char in line_stripped:
                row.append(char)
    return grid


def print_energy(grid, visited):
    print()
    for x, row in enumerate(grid):
        string = ""
        for y, char in enumerate(row):
            if (x, y) in visited:
                string += "# "
            else:
                string += ". "
        print(string)
    print()


def print_grid(grid):
    print()
    for row in grid:
        string = ""
        for char in row:
            string += char + " "
        print(string)
    print()


def compute(grid, start):
    X = len(grid)
    Y = len(grid[0])

    visited_positions = []
    visited = []
    Q = [start]
    while len(Q) > 0:
        node = Q.pop()
        x, y, dx, dy = node
        nx = x + dx
        ny = y + dy

        if not 0 <= nx < X or not 0 <= ny < Y:
            continue

        # print(f"{nx} - {ny}")
        if (nx, ny) not in visited_positions:
            visited_positions.append((nx, ny))
        char = grid[nx][ny]

        if char == ".":
            ndx = dx
            ndy = dy
            next_node = (nx, ny, ndx, ndy)
            if next_node not in visited:
                visited.append(next_node)
                Q.append(next_node)
        elif char == "/":
            ndx = -dy
            ndy = -dx
            next_node = (nx, ny, ndx, ndy)
            if next_node not in visited:
                visited.append(next_node)
                Q.append(next_node)
        elif char == "\\":
            ndx = dy
            ndy = dx
            next_node = (nx, ny, ndx, ndy)
            if next_node not in visited:
                visited.append(next_node)
                Q.append(next_node)
        elif char == "-":
            if dx == 0:
                ndx = dx
                ndy = dy
                next_node = (nx, ny, ndx, ndy)
                if next_node not in visited:
                    visited.append(next_node)
                    Q.append(next_node)
            else:
                ndx = 0
                ndy1 = 1
                ndy2 = -1
                next_node_1 = (nx, ny, ndx, ndy1)
                next_node_2 = (nx, ny, ndx, ndy2)
                if next_node_1 not in visited:
                    visited.append(next_node_1)
                    Q.append(next_node_1)
                if next_node_2 not in visited:
                    visited.append(next_node_2)
                    Q.append(next_node_2)
        elif char == "|":
            if dy == 0:
                ndx = dx
                ndy = dy
                next_node = (nx, ny, ndx, ndy)
                if next_node not in visited:
                    visited.append(next_node)
                    Q.append(next_node)
            else:
                ndy = 0
                ndx1 = 1
                ndx2 = -1
                next_node_1 = (nx, ny, ndx1, ndy)
                next_node_2 = (nx, ny, ndx2, ndy)
                if next_node_1 not in visited:
                    visited.append(next_node_1)
                    Q.append(next_node_1)
                if next_node_2 not in visited:
                    visited.append(next_node_2)
                    Q.append(next_node_2)

    #print_energy(grid, visited_positions)
    res = len(visited_positions)
    return res


def a():
    res = 0
    grid = parse_input()

    X = len(grid)
    Y = len(grid[0])
    print(X)
    print(Y)
    print_grid(grid)

    res = compute(grid, (0, -1, 0, 1))

    return res


def b():
    res = 0
    grid = parse_input()

    X = len(grid)
    Y = len(grid[0])
    print(X)
    print(Y)
    print_grid(grid)

    for x in range(X):
        for y in [-1, Y]:
            print(f"{x} - {y}")
            dx = 0
            if y == -1:
                dy = 1
            else:
                dy = -1

            start = (x, y, dx, dy)
            value = compute(grid, start)
            if value > res:
                res = value

    for y in range(Y):
        for x in [-1, X]:
            print(f"{x} - {y}")
            dy = 0
            if x == -1:
                dx = 1
            else:
                dx = -1

            start = (x, y, dx, dy)
            value = compute(grid, start)
            if value > res:
                res = value

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
