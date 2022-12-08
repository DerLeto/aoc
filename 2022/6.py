from copy import deepcopy
from enum import Enum

input_path = "input/6.txt"


def a():
    with open(input_path) as file:
        window = []
        for i, character in enumerate(file.read()):
            if character not in window:
                window.append(character)
                if len(window) == 4:
                    return i + 1
            else:
                copy = window[window.index(character) + 1:]
                window.clear()
                window.extend(copy)
                window.append(character)


def b():
    with open(input_path) as file:
        window = []
        for i, character in enumerate(file.read()):
            if character not in window:
                window.append(character)
                if len(window) == 14:
                    return i + 1
            else:
                copy = window[window.index(character) + 1:]
                window.clear()
                window.extend(copy)
                window.append(character)


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
