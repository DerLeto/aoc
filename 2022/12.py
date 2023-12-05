import sys

import numpy as np

input_path = "input/12.txt"

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def traverse(array, poses, visited, depth, des_value, des_function, forward):
    new_poses = []
    if len(poses) == 0:
        print("=== ERROR ===")
        return 0
    for pos in poses:
        if des_function(array, pos, des_value):
            return depth
        for dir in dirs:
            new_pos = (pos[0] + dir[0], pos[1] + dir[1])
            if not 0 <= new_pos[0] < array.shape[0] or not 0 <= new_pos[1] < array.shape[1]:
                continue
            if new_pos in visited:
                continue
            if forward and array[new_pos] - array[pos] > 1:
                continue
            if not forward and array[pos] - array[new_pos] > 1:
                continue
            new_poses.append(new_pos)
            visited.append(new_pos)

    return traverse(array, new_poses, visited, depth + 1, des_value, des_function, forward)


def is_destination_a(array, pos, end_pos):
    return pos == end_pos


def is_destination_b(array, pos, des_height):
    return array[pos] == des_height


def parse():
    with open(input_path) as file:
        data = file.read().strip()

    lines = data.split("\n")
    array = np.zeros(shape=(len(lines), len(lines[0])), dtype=int)
    start = (0, 0)
    end = (0, 0)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "S":
                array[i, j] = 0
                start = (i, j)
            elif char == "E":
                array[i, j] = 25
                end = (i, j)
            else:
                array[i, j] = ord(char) - ord("a")

    return array, start, end


def a():
    array, start, end = parse()
    res = traverse(array, [start], [start], 0, end, is_destination_a, True)
    return res


def b():
    array, start, end = parse()
    res = traverse(array, [end], [end], 0, 0, is_destination_b, False)
    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
