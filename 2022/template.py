input_path = "input/x.txt"

def a():
    res = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()

    return res


def b():
    res = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
