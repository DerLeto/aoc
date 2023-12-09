from math import lcm

input_path = "input/8.txt"


def a():
    res = 0
    with open(input_path) as file:
        directions, mapping = file.read().strip().split("\n\n")

    directions = directions.strip()

    instructions = {}
    for line in mapping.strip().split("\n"):
        line_stripped = line.strip()
        source, targets = line_stripped.split("=")
        left, right = targets.strip().replace("(", "").replace(")", "").split(",")
        instructions[source.strip()] = {
            "L": left.strip(),
            "R": right.strip()
        }

    start = "AAA"
    end = "ZZZ"

    current = start
    while not current == end:
        for direction in directions:
            res += 1
            current = instructions[current][direction]

            if current == end:
                break

    return res


def b():
    res = 0
    with open(input_path) as file:
        directions, mapping = file.read().strip().split("\n\n")

    directions = directions.strip()

    instructions = {}
    start_nodes = []
    end_nodes = []
    for line in mapping.strip().split("\n"):
        line_stripped = line.strip()
        source, targets = line_stripped.split("=")
        left, right = targets.strip().replace("(", "").replace(")", "").split(",")
        instructions[source.strip()] = {
            "L": left.strip(),
            "R": right.strip()
        }

        if source.strip().endswith("A"):
            start_nodes.append(source.strip())

        if source.strip().endswith("Z"):
            end_nodes.append(source.strip())

    steps = []
    for node in start_nodes:
        counter = 0
        current = node
        while not current.endswith("Z"):
            for direction in directions:
                counter += 1
                current = instructions[current][direction]

                if current.endswith("Z"):
                    steps.append(counter)
                    break

    print(steps)
    res = lcm(*steps)
    return res

    # while not finished(current_nodes):
    #     print(res)
    #     for direction in directions:
    #         res += 1
    #
    #         next_nodes = []
    #         for node in current_nodes:
    #             next_node = instructions[node][direction]
    #             next_nodes.append(next_node)
    #
    #         current_nodes = next_nodes
    #         if finished(current_nodes):
    #             break
    #
    # return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
