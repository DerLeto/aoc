input_path = "input/9.txt"


def a():
    res = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            values = [int(value.strip()) for value in line_stripped.split()]

            necessary_values = []
            while not all(v == 0 for v in values):
                next_values = []
                last_value = values[0]
                for value in values[1:]:
                    next_value = value - last_value
                    next_values.append(next_value)
                    last_value = value
                necessary_values.append(values[-1])
                values = next_values

            next_value = 0
            for value in necessary_values:
                next_value += value

            res += next_value

    return res


def b():
    res = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            values = [int(value.strip()) for value in line_stripped.split()]

            print(values)
            necessary_values = []
            while not all(v == 0 for v in values):
                next_values = []
                last_value = values[0]
                for value in values[1:]:
                    next_value = value - last_value
                    next_values.append(next_value)
                    last_value = value
                necessary_values.append(values[0])
                values = next_values
                print(values)

            next_value = 0
            for value in necessary_values[::-1]:
                print(next_value)
                next_value = value - next_value

            res += next_value
            print(necessary_values)
            print(next_value)
            print()

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
