import numpy as np

input_path = "input/17.txt"


def print_visited(grid, visited):
    X, Y = grid.shape
    visited_grid = np.zeros(shape=(X, Y), dtype=int)
    for (x, y), loss in visited.items():
        visited_grid[x, y] = loss
    print(visited_grid)


def print_path(grid, path, last_node):
    X, Y = grid.shape
    visited_grid = np.zeros(shape=(X, Y), dtype=int)

    node = last_node
    while not node == (0, 0, 0):
        x, y, loss = node
        visited_grid[x, y] = loss
        node = path[node]

    print(visited_grid)


def parse_grid():
    with open(input_path) as file:
        data = file.read().strip().split("\n")

    X = len(data)
    Y = len(data[0])

    grid = np.zeros(shape=(X, Y), dtype=int)
    for x, row in enumerate(data):
        for y, char in enumerate(row):
            grid[x, y] = int(char)

    return grid


def append_node(x, y, dx, dy, loss, Q, visited):
    if (x, y, dx, dy) in visited:
        last_loss = visited.get((x, y, dx, dy))
        if loss > last_loss:
            return

    if (x, y, dx, dy, loss) in Q:
        return
    Q.append((x, y, dx, dy, loss))


def astar(grid, min, max):
    X, Y = grid.shape

    Q = []
    visited = {}
    path = {}
    Q.append((0, 0, 0, 0, 0))

    last_node = None
    while len(Q) > 0:
        # print(Q)
        node = Q.pop()
        print(node)
        x, y, dx, dy, loss = node

        if (x, y, dx, dy) in visited:
            last_loss = visited.get((x, y, dx, dy))
            if loss > last_loss:
                continue

        visited[(x, y, dx, dy)] = loss

        if x == X - 1 and y == Y - 1:
            #print_visited(grid, visited)
            print_path(grid, path, (x, y, loss))
            return loss

        if not dx == 0:
            if abs(dx) >= min and y < Y - 1:
                nx = x
                ny = y + 1
                ndx = 0
                ndy = 1
                nloss = loss + grid[nx, ny]
                path[nx, ny, nloss] = (x, y, loss)
                append_node(nx, ny, ndx, ndy, nloss, Q, visited)
            if abs(dx) >= min and y > 0:
                nx = x
                ny = y - 1
                ndx = 0
                ndy = -1
                nloss = loss + grid[nx, ny]
                path[nx, ny, nloss] = (x, y, loss)
                append_node(nx, ny, ndx, ndy, nloss, Q, visited)
            if 0 < dx < max and x < X - 1:
                nx = x + 1
                ny = y
                ndx = dx + 1
                ndy = 0
                nloss = loss + grid[nx, ny]
                path[nx, ny, nloss] = (x, y, loss)
                append_node(nx, ny, ndx, ndy, nloss, Q, visited)
            if -max < dx < 0 and x > 0:
                nx = x - 1
                ny = y
                ndx = dx - 1
                ndy = 0
                nloss = loss + grid[nx, ny]
                path[nx, ny, nloss] = (x, y, loss)
                append_node(nx, ny, ndx, ndy, nloss, Q, visited)
        else:
            if 0 <= dy < max and y < Y - 1:
                nx = x
                ny = y + 1
                ndx = 0
                ndy = dy + 1
                nloss = loss + grid[nx, ny]
                path[nx, ny, nloss] = (x, y, loss)
                append_node(nx, ny, ndx, ndy, nloss, Q, visited)
            if -max < dy < 0 and y > 0:
                nx = x
                ny = y - 1
                ndx = 0
                ndy = dy - 1
                nloss = loss + grid[nx, ny]
                path[nx, ny, nloss] = (x, y, loss)
                append_node(nx, ny, ndx, ndy, nloss, Q, visited)
            if abs(dy) >= min and x < X - 1:
                nx = x + 1
                ny = y
                ndx = 1
                ndy = 0
                nloss = loss + grid[nx, ny]
                path[nx, ny, nloss] = (x, y, loss)
                append_node(nx, ny, ndx, ndy, nloss, Q, visited)
            if abs(dy) >= min and x > 0:
                nx = x - 1
                ny = y
                ndx = -1
                ndy = 0
                nloss = loss + grid[nx, ny]
                path[nx, ny, nloss] = (x, y, loss)
                append_node(nx, ny, ndx, ndy, nloss, Q, visited)

        Q.sort(key=lambda node: node[-1], reverse=True)


def a():
    grid = parse_grid()
    print(grid)
    res = astar(grid, 1, 3)

    return res


def b():
    grid = parse_grid()
    print(grid)
    res = astar(grid, 4, 10)

    return res


def main():
    #res_a = a()
    res_b = b()
    #print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
