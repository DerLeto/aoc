input_path = "input/6.txt"


def a():
    res = 1
    with open(input_path) as file:
        data = file.read()

    times, distances = data.split("\n")[0:2]
    times = [int(time) for time in times.strip().split()[1:]]
    distances = [int(distance) for distance in distances.strip().split()[1:]]

    for time, goal_distance in zip(times, distances):
        counter = 0
        for i in range(time):
            speed = i
            travel_time = time - i
            distance = travel_time * speed
            if distance > goal_distance:
                counter += 1

        res *= counter

    return res


def b():
    res = 1
    with open(input_path) as file:
        data = file.read()

    times, distances = data.split("\n")[0:2]
    time = int(times.split(":")[1].replace(" ", ""))
    goal_distance = int(distances.split(":")[1].replace(" ", ""))

    counter = 0
    for i in range(time):
        speed = i
        travel_time = time - i
        distance = travel_time * speed
        if distance > goal_distance:
            counter += 1

    res *= counter

    return res


def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
