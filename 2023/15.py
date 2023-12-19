input_path = "input/15.txt"

def a():
    res = 0
    with open(input_path) as file:
        data = file.read().strip()

    words = [word.strip() for word in data.split(",")]
    for word in words:
        value = 0
        for char in word:
            value += ord(char)
            value *= 17
            value %= 256
        res += value

    return res


def b():
    res = 0
    with open(input_path) as file:
        data = file.read().strip()

    words = [word.strip() for word in data.split(",")]
    boxes = {}

    for i in range(256):
        boxes[i] = []

    for word in words:
        if word.endswith("-"):
            label = word[:-1]
            operation = "-"
        else:
            label, focus = word.rsplit("=", 2)
            operation = "="

        value = 0
        for char in label:
            value += ord(char)
            value *= 17
            value %= 256
        print(value)

        if operation == "=":
            add_lens(boxes.get(value), label, int(focus))
        else:
            remove_lens(boxes.get(value), label)

    for box, lenses in boxes.items():
        for i, (lens, focus) in enumerate(lenses):
            res += (box + 1) * (i + 1) * focus

    return res


def add_lens(box: list, new_lens: str, new_focus: int):
    contains = -1
    for i, (lens, focus) in enumerate(box):
        if lens == new_lens:
            contains = i

    if contains > -1:
        box[contains] = (new_lens, new_focus)
    else:
        box.append((new_lens, new_focus))


def remove_lens(box: list, lens_to_remove: str):
    item = None
    for i, (lens, focus) in enumerate(box):
        if lens == lens_to_remove:
            item = (lens, focus)

    if item is not None:
        box.remove(item)


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
