import numpy as np

input_path = "input/3.txt"


def parse(data: str) -> np.array:
    lines = data.split("\n")
    array = np.zeros(shape=(len(lines), len(lines[0])), dtype=int)

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            char: str = char
            if char.isnumeric():
                array[i, j] = int(char)
            elif char == ".":
                array[i, j] = -1
            elif char == "*":
                array[i, j] = 11
            else:
                array[i, j] = 10

    return array


def check_adjacent(array, indeces) -> bool:
    for index in indeces:
        x, y = index

        if x > 0 and array[x - 1, y] >= 10:
            return True
        if x > 0 and y > 0 and array[x - 1, y - 1] >= 10:
            return True
        if x > 0 and y < array.shape[1] - 1 and array[x - 1, y + 1] >= 10:
            return True
        if x < array.shape[0] - 1 and array[x + 1, y] >= 10:
            return True
        if x < array.shape[0] - 1 and y > 0 and array[x + 1, y - 1] >= 10:
            return True
        if x < array.shape[0] - 1 and y < array.shape[1] - 1 and array[x + 1, y + 1] >= 10:
            return True
        if y > 0 and array[x, y - 1] >= 10:
            return True
        if y < array.shape[1] - 1 and array[x, y + 1] >= 10:
            return True

    return False


def find_gears(array, indeces) -> list:
    gears = set()
    for index in indeces:
        x, y = index

        if x > 0 and array[x - 1, y] == 11:
            gears.add((x - 1, y))
        if x > 0 and y > 0 and array[x - 1, y - 1] == 11:
            gears.add((x - 1, y - 1))
        if x > 0 and y < array.shape[1] - 1 and array[x - 1, y + 1] == 11:
            gears.add((x - 1, y + 1))
        if x < array.shape[0] - 1 and array[x + 1, y] == 11:
            gears.add((x + 1, y))
        if x < array.shape[0] - 1 and y > 0 and array[x + 1, y - 1] == 11:
            gears.add((x + 1, y - 1))
        if x < array.shape[0] - 1 and y < array.shape[1] - 1 and array[x + 1, y + 1] == 11:
            gears.add((x + 1, y + 1))
        if y > 0 and array[x, y - 1] == 11:
            gears.add((x, y - 1))
        if y < array.shape[1] - 1 and array[x, y + 1] == 11:
            gears.add((x, y + 1))

    return list(gears)


def a():
    res = 0
    with open(input_path) as file:
        array = parse(file.read())

    print(array)
    rows = array.shape[0]
    cols = array.shape[1]

    for x in range(0, rows):
        indeces = []
        number = 0
        for y in range(0, cols):
            field = array[x, y]
            if 0 <= field <= 9:
                number = number * 10 + field
                indeces.append((x, y))
            else:
                if check_adjacent(array, indeces):
                    print(number)
                    res += number
                indeces = []
                number = 0

        if check_adjacent(array, indeces):
            print(number)
            res += number
        indeces = []
        number = 0

    return res


def b():
    res = 0
    with open(input_path) as file:
        array = parse(file.read())

    print(array)
    rows = array.shape[0]
    cols = array.shape[1]

    gears = {}
    for x in range(0, rows):
        indeces = []
        number = 0
        for y in range(0, cols):
            field = array[x, y]
            if 0 <= field <= 9:
                number = number * 10 + field
                indeces.append((x, y))
            else:
                gears_found = find_gears(array, indeces)
                for gear in gears_found:
                    if gear not in gears:
                        gears[gear] = []
                    gears[gear].append(number)
                indeces = []
                number = 0

        gears_found = find_gears(array, indeces)
        for gear in gears_found:
            if gear not in gears:
                gears[gear] = []
            gears[gear].append(number)
        indeces = []
        number = 0

    for gear, numbers in gears.items():
        if len(numbers) == 2:
            res += numbers[0] * numbers[1]

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
