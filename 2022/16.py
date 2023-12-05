input_path = "input/16.ex"

class Pipe:
    def __init__(self, name, flow_rate, childs):
        self.name = name
        self.flow_rate = flow_rate
        self.childs = childs


def parse():
    pipes = {}
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            words = line_stripped.split()
            name = words[1]
            flow_rate = int(words[4].split(";")[0].split("=")[1])
            childs = []
            for i in range(9, len(words)):
                childs.append(words[i].split(";")[0])

            pipes[name] = Pipe(name, flow_rate, childs)
    return pipes

def a():
    res = 0
    pipes = parse()

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
