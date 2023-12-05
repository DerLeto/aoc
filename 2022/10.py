input_path = "input/10.txt"

interesting_cycles = [20, 60, 100, 140, 180, 220]
lines_end = [40, 80, 120, 160, 200, 240]

def a():
    res = 0
    with open(input_path) as file:
        cycles = 0
        value = 1
        for line in file:
            line_stripped = line.strip()
            words = line_stripped.split()
            if words[0] == "noop":
                cycles += 1
                if cycles in interesting_cycles:
                    res += cycles * value
            else:
                dvalue = int(words[1])
                cycles += 1
                if cycles in interesting_cycles:
                    res += cycles * value

                cycles += 1
                if cycles in interesting_cycles:
                    res += cycles * value
                value += dvalue

    return res


def b():
    res = 0
    with open(input_path) as file:
        cycles = 0
        drawing_pos = -1
        value = 1
        for line in file:
            line_stripped = line.strip()
            words = line_stripped.split()
            if words[0] == "noop":
                ticks = 1
                value_update = 0
            else:
                ticks = 2
                value_update = int(words[1])

            for i in range(ticks):
                cycles += 1
                drawing_pos += 1
                if value-1 <= drawing_pos <= value+1:
                    print('#', end='')
                else:
                    print('.', end='')
                if cycles in lines_end:
                    print()
                    drawing_pos = -1

            value += value_update

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
