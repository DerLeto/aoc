input_path = "input/18.ex"

def a():
    res = 0
    points = {}
    corners = {}
    with open(input_path) as file:
        x = 0
        y = 0
        last = "?"
        for line in file:
            line_stripped = line.strip()
            dir, steps, color = line_stripped.split()
            steps = int(steps)
            char = 0
            if dir == "U":
                if last in ["L", "R"]:
                    corners[(x, y)] = 1
                else:
                    corners[(x, y)] = 0
                char = 1
                dx = 1
                dy = 0
            elif dir == "D":
                corners[(x, y)] = 0
                char = 1
                dx = -1
                dy = 0
            elif dir == "L":
                if last in ["D"]:
                    corners[(x, y)] = 1
                else:
                    corners[(x, y)] = 0
                dx = 0
                dy = -1
            elif dir == "R":
                if last in ["D"]:
                    corners[(x, y)] = 1
                else:
                    corners[(x, y)] = 0
                dx = 0
                dy = 1

            for i in range(steps):
                nx = x + dx * i
                ny = y + dy * i
                if nx not in points:
                    points[nx] = []
                points[nx].append(ny)

                if (nx, ny) not in corners:
                    corners[(nx, ny)] = char

            x = x + dx * steps
            y = y + dy * steps
            last = dir

    print(points)
    print(corners)
    for x, ys in points.items():
        ys.sort()
        print(ys)
        inside = False
        for y in range(ys[0], ys[-1] + 1):
            if (x, y) in corners and corners[(x, y)] == 1:
                inside = not inside

            if y in ys:
                continue

            if inside:
                res += 1
        res += len(ys)
        print(res)

    return res


def b():
    res = 0
    points = {}
    corners = {}
    with open(input_path) as file:
        x = 0
        y = 0
        last = "?"
        for line in file:
            line_stripped = line.strip()
            dir, steps, color = line_stripped.split()

            color = color.replace("(#", "")
            color = color.replace(")", "")
            dir = ["R", "D", "L", "U"][int(color[-1])]
            steps = int(color[0:-1], 16)
            print(dir)
            print(steps)

            char = 0
            if dir == "U":
                if last in ["L", "R"]:
                    corners[(x, y)] = 1
                else:
                    corners[(x, y)] = 0
                char = 1
                dx = 1
                dy = 0
            elif dir == "D":
                corners[(x, y)] = 0
                char = 1
                dx = -1
                dy = 0
            elif dir == "L":
                if last in ["D"]:
                    corners[(x, y)] = 1
                else:
                    corners[(x, y)] = 0
                dx = 0
                dy = -1
            elif dir == "R":
                if last in ["D"]:
                    corners[(x, y)] = 1
                else:
                    corners[(x, y)] = 0
                dx = 0
                dy = 1

            for i in range(steps):
                nx = x + dx * i
                ny = y + dy * i
                if nx not in points:
                    points[nx] = []
                points[nx].append(ny)

                if (nx, ny) not in corners:
                    corners[(nx, ny)] = char

            x = x + dx * steps
            y = y + dy * steps
            last = dir

    #print(points)
    #print(corners)
    for x, ys in points.items():
        ys.sort()
        #print(ys)
        inside = False
        for y in range(ys[0], ys[-1] + 1):
            if (x, y) in corners and corners[(x, y)] == 1:
                inside = not inside

            if y in ys:
                continue

            if inside:
                res += 1
        res += len(ys)
        #print(res)

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
