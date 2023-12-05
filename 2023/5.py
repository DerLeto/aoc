input_path = "input/5.txt"


def a():
    res = 0
    seeds = []
    with open(input_path) as file:
        parts = file.read().strip().split("\n\n")

        # seeds
        seeds_string = parts[0].strip().split(":")[1]
        for seed in seeds_string.strip().split():
            seeds.append(int(seed.strip()))

        # soil
        previous = [seed for seed in seeds]
        for part in parts[1:]:
            next = [entry for entry in previous]
            for line in part.strip().split("\n")[1:]:
                des, source, range_nr = line.strip().split()
                des = int(des.strip())
                source = int(source.strip())
                range_nr = int(range_nr.strip())

                for i in range(len(previous)):
                    if source <= previous[i] < source + range_nr:
                        next[i] = des + (previous[i] - source)

            previous = next

    res = min(previous)

    return res


def b():
    res = 0
    seeds = []
    with open(input_path) as file:
        parts = file.read().strip().split("\n\n")

    # seeds
    seeds_string = parts[0].strip().split(":")[1]
    seeds_parts = seeds_string.strip().split()

    ranges = []
    for i in range(0, len(seeds_parts), 2):
        start = int(seeds_parts[i].strip())
        range_nr = int(seeds_parts[i + 1].strip())
        ranges.append((start, range_nr))


    previous = [entry for entry in ranges]
    for part in parts[1:]:
        next = []
        to_check = [entry for entry in previous]
        print(previous)
        for line in part.strip().split("\n")[1:]:
            des, source, range_nr = line.strip().split()
            des = int(des.strip())
            source = int(source.strip())
            range_nr = int(range_nr.strip())

            to_check_next = []
            for start, r in to_check:
                end = start + r
                if source <= start <= source + range_nr and source <= end <= source + range_nr:
                    next.append((des + start - source, r))

                elif start <= source and source + range_nr <= end:
                    next.append((des, range_nr))
                    to_check_next.append((start, source - start))
                    to_check_next.append((source + range_nr, end - (source + range_nr)))
                elif start <= source and source <= end <= source + range_nr:
                    next.append((des, end - source))
                    to_check_next.append((start, source - start))
                elif source <= start <= source + range_nr and end >= source + range_nr:
                    next.append((des + (start - source), source + range_nr - start))
                    to_check_next.append((source + range_nr, end - (source + range_nr)))
                else:
                    to_check_next.append((start, r))
            to_check = to_check_next

        for start, r in to_check:
            next.append((start, r))
        previous = next

    print(previous)
    res = min([start for start, r in previous])

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
