import numpy as np

input_path = "input/8.txt"

def getArray():
    with open(input_path) as file:
        lines = [line.strip() for line in file]
        array = np.zeros(shape=(len(lines), len(lines[0])))
        for i, line in enumerate(lines):
            for j, char in enumerate(line):
                array[i, j] = int(char)

    print(array)
    return array

def a():
    res = 0
    array = getArray()

    for i, j in np.ndindex(array.shape):
        if i == 0 or j == 0 or i == array.shape[0] - 1 or j == array.shape[0] - 1:
            res += 1
        # above
        elif np.max(array[0:i,j]) < array[i,j]:
            res += 1
        # below
        elif np.max(array[i+1:,j]) < array[i,j]:
            res += 1
        # right
        elif np.max(array[i, 0:j]) < array[i, j]:
            res += 1
        # left
        elif np.max(array[i, j+1:]) < array[i, j]:
            res += 1

    return res


def b():
    res = 0
    index = (0, 0)
    array = getArray()

    for i, j in np.ndindex(array.shape):
        current_score = 1

        for set in [np.flip(array[0:i, j]), array[i + 1:, j], np.flip(array[i, 0:j]), array[i, j + 1:]]:
            score = 0
            for tree in set:
                if tree < array[i, j]:
                    score += 1
                else:
                    score += 1
                    break
            current_score *= score

        if current_score > res:
            res = current_score
            index = (i, j)

    print(index)
    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
