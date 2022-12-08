input_path = "input/7.txt"


def a():
    res = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()

    return res


def b():
    return 0


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
