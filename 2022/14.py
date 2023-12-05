import numpy as np

input_path = "input/14.txt"

class Line:
    def __init__(self, start, end):
        if start[0] < end[0] or start[1] < end[1]:
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start

    def __str__(self):
        return str(self.start) + " -> " + str(self.end)

    def __repr__(self):
        return str(self)

def parse():
    max_x = 0
    max_y = 0
    lines = []
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            points = line_stripped.split(" -> ")
            current_point = None
            for point in points:
                x, y = point.split(",")
                x = int(x)
                y = int(y)
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y
                if current_point is not None:
                    lines.append(Line(current_point, (x, y)))
                current_point = (x, y)

    print(max_x)
    print(max_y)
    print(lines)

    array = np.zeros(shape=(max_x * 2, max_y + 3))
    return lines, array

def fill_array(array, lines):
    for line in lines:
        start = line.start
        end = line.end

        for x in range(start[0], end[0] + 1):
            for y in range(start[1], end[1] + 1):
                # print(x, y)
                array[x, y] = 1
        # print(array[494:504, 0:10])

    return array

def a():
    res = 0
    lines, array = parse()
    array = fill_array(array, lines)

    void_reached = 0
    while not void_reached:
        x = 500
        y = 0
        while True:
            if not 0 <= y + 1 < array.shape[1]:
                void_reached = True
                break
            elif array[x, y+1] == 0:
                y = y + 1
            elif array[x-1, y+1] == 0:
                x = x - 1
                y = y + 1
            elif array[x+1, y+1] == 0:
                x = x + 1
                y = y + 1
            else:
                array[x, y] = 2
                res += 1
                break

    return res


def b():
    res = 0
    lines, array = parse()
    array = fill_array(array, lines)

    for x in range(array.shape[0]):
        array[x, array.shape[1] - 1] = 3

    void_reached = 0
    while not void_reached:
        x = 500
        y = 0

        if not array[x, y] == 0:
            void_reached = True
            break

        while True:
            if array[x, y + 1] == 0:
                y = y + 1
            elif array[x - 1, y + 1] == 0:
                x = x - 1
                y = y + 1
            elif array[x + 1, y + 1] == 0:
                x = x + 1
                y = y + 1
            else:
                array[x, y] = 2
                res += 1
                break

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
