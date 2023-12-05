input_path = "input/1.txt"

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def a():
    res = 0
    with open(input_path) as file:
        for line in file:
            line_forward = line.strip()
            line_backward = line_forward[::-1]

            number = 0
            for char in line_forward:
                if char.isnumeric():
                    number += int(char) * 10
                    break

            for char in line_backward:
                if char.isnumeric():
                    number += int(char)
                    break

            res += number

    return res


def b():
    res = 0
    with open(input_path) as file:
        for line in file:
            line_forward = line.strip()
            line_forward = replaceStringByNumber(line_forward)

            line_backward = line.strip()
            line_backward = line_backward[::-1]
            line_backward = replaceStringByNumber(line_backward, True)


            number = 0
            for char in line_forward:
                if char.isnumeric():
                    number += int(char) * 10
                    break

            for char in line_backward:
                if char.isnumeric():
                    number += int(char)
                    break

            res += number

    return res


def replaceStringByNumber(input: str, rev: bool = False):
    result = input

    part = ""
    for char in input:
        if not rev:
            part += char
        else:
            part = char + part

        for number in numbers.keys():
            if number in part:
                if not rev:
                    result = result.replace(number, numbers.get(number), 1)
                else:
                    result = result.replace(number[::-1], numbers.get(number), 1)
                part = ""

    return result


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
