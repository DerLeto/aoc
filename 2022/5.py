import re

input_path = "input/5.txt"


def a():
    message = ""
    with open(input_path) as file:
        lines = file.read()

    begin, commands = lines.split("\n\n")
    stacks = [[] for i in range(9)]
    begin_split = begin.split("\n")
    begin_split.reverse()
    for line in begin_split:
        if line[1].isdigit():
            continue
        pointer = 1
        for stack in stacks:
            if not line[pointer] == " ":
                stack.append(line[pointer])
            pointer += 4

    for command in commands.strip().split("\n"):
        parts = [int(s) for s in re.findall(r'\b\d+\b', command)]
        for i in range(parts[0]):
            create = stacks[parts[1] - 1].pop()
            stacks[parts[2] - 1].append(create)

    for stack in stacks:
        message += stack[-1]

    return message


def b():
    message = ""
    with open(input_path) as file:
        lines = file.read()

    begin, commands = lines.split("\n\n")
    stacks = [[] for i in range(9)]
    begin_split = begin.split("\n")
    begin_split.reverse()
    for line in begin_split:
        if line[1].isdigit():
            continue
        pointer = 1
        for stack in stacks:
            if not line[pointer] == " ":
                stack.append(line[pointer])
            pointer += 4

    for command in commands.strip().split("\n"):
        parts = [int(s) for s in re.findall(r'\b\d+\b', command)]
        buffer = []
        for i in range(parts[0]):
            create = stacks[parts[1] - 1].pop()
            buffer.append(create)
        buffer.reverse()
        stacks[parts[2] - 1].extend(buffer)
        buffer.clear()

    for stack in stacks:
        message += stack[-1]

    return message


def main():
    points_a = a()
    points_b = b()
    print("a: " + str(points_a))
    print("b: " + str(points_b))


if __name__ == "__main__":
    main()
