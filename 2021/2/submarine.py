from sys import argv


def task_1(data):
    pos = 0
    height = 0
    for line in data:
        if line[0:-3] == "forward":
            pos += int(line[-2])
        elif line[0:-3] == "down":
            height += int(line[-2])
        elif line[0:-3] == "up":
            height -= int(line[-2])
        else:
            print("ERROR: " + line[0:-3])

    return pos, height


def task_2(data):
    pos = 0
    depth = 0
    aim = 0
    for line in data:
        if line[0:-3] == "forward":
            value = int(line[-2])
            pos += value
            depth += aim * value
        elif line[0:-3] == "down":
            aim += int(line[-2])
        elif line[0:-3] == "up":
            aim -= int(line[-2])
        else:
            print("ERROR: " + line[0:-3])

    return pos, depth


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: <path to input>")
        exit(0)

    file = argv[1]
    data = open(file)
    position, height = task_2(data)
    print("Position: " + str(position) + " | Height: " + str(height))
    print("Result: " + str(position * height))

