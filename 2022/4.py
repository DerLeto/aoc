from enum import Enum

input_path = "input/4.txt"


def a():
    points = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            section1, section2 = line_stripped.split(",")
            min1, max1 = [int(part) for part in section1.split("-")]
            min2, max2 = [int(part) for part in section2.split("-")]
            if (min1 <= min2 and max1 >= max2) or (min2 <= min1 and max2 >= max1):
                points += 1
    return points


def b():
    points = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            section1, section2 = line_stripped.split(",")
            min1, max1 = [int(part) for part in section1.split("-")]
            min2, max2 = [int(part) for part in section2.split("-")]
            if min2 <= min1 <= max2 or min2 <= max1 <= max2 or min1 <= min2 <= max1 or min1 <= max2 <= max1:
                points += 1
    return points


def main():
    points = b()
    print("Points: " + str(points))


if __name__ == "__main__":
    main()
