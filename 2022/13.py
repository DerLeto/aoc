import ast
import functools

input_path = "input/13.txt"

def check(a, b):
    for itema, itemb in zip(a, b):
        # print(itema, itemb)
        if isinstance(itema, int) and isinstance(itemb, int):
            if itema > itemb:
                return -1
            elif itema < itemb:
                return 1
        else:
            itema = itema if isinstance(itema, list) else [itema]
            itemb = itemb if isinstance(itemb, list) else [itemb]
            result = check(itema, itemb)
            if not result == 0:
                return result

    if len(a) > len(b):
        return -1
    elif len(a) < len(b):
        return 1
    else:
        return 0

def a():
    res = 0
    with open(input_path) as file:
        data = file.read().strip()

    for i, pair in enumerate(data.split("\n\n")):
        a, b = pair.split("\n")
        a = ast.literal_eval(a)
        b = ast.literal_eval(b)
        # print(a, b)
        status = check(a, b)
        print(i+1, ": ", status)
        if status == 1:
            res += i+1

    return res


def b():
    res = 0
    with open(input_path) as file:
        data = file.read().strip()

    divider1 = [[2]]
    divider2 = [[6]]
    packets = [divider1, divider2]
    for i, pair in enumerate(data.split("\n\n")):
        a, b = pair.split("\n")
        a = ast.literal_eval(a)
        b = ast.literal_eval(b)
        packets.append(a)
        packets.append(b)

    print(packets)
    packets.sort(key=functools.cmp_to_key(check))
    packets.reverse()
    print(packets)

    return (packets.index(divider1) + 1) * (packets.index(divider2) + 1)


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
