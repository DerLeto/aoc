import math
import re

import numpy as np

input_path = "input/15.txt"

class Sensor:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.position = (x, y)
        self.distance = distance


def compute_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a():
    return 0
    res = 0
    beacons = []
    sensors = []
    min_x = 1000000
    max_x = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            x_sensor, y_sensor, x_beacon, y_beacon = [int(s) for s in re.findall(r'[-+]?\b\d+\b', line_stripped)]
            #print(x_sensor, y_sensor, x_beacon, y_beacon)
            d = compute_distance((x_sensor, y_sensor), (x_beacon, y_beacon))
            sensors.append(Sensor(x_sensor, y_sensor, d))
            beacons.append((x_beacon, y_beacon))
            #print(d)
            if x_sensor - d < min_x:
                min_x = x_sensor - d
            if x_sensor + d > max_x:
                max_x = x_sensor + d

    print(min_x, max_x)

    y = 10
    found = []
    for sensor in sensors:
        d = compute_distance(sensor.position, (sensor.x, y))
        if d > sensor.distance:
            continue
        dx = sensor.distance - d
        for x in range(sensor.x - dx, sensor.x + dx + 1):
            if (x, y) in beacons:
                continue
            if (x, y) not in found:
                found.append((x, y))
                res += 1

    # for x in range(min_x, max_x + 1):
    #     if (x, y) in beacons:
    #         continue
    #     for sensor in sensors:
    #         if (x, y) == sensor.position:
    #             res += 1
    #             break
    #         d = compute_distance(sensor.position, (x, y))
    #         if d <= sensor.distance:
    #             res += 1
    #             break

    return res


def b():
    res = 0
    length = 4000001
    #length = 21
    beacons = []
    sensors = []
    min_x = 1000000
    max_x = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            x_sensor, y_sensor, x_beacon, y_beacon = [int(s) for s in re.findall(r'[-+]?\b\d+\b', line_stripped)]
            # print(x_sensor, y_sensor, x_beacon, y_beacon)
            d = compute_distance((x_sensor, y_sensor), (x_beacon, y_beacon))
            sensors.append(Sensor(x_sensor, y_sensor, d))
            beacons.append((x_beacon, y_beacon))
            # print(d)
            if x_sensor - d < min_x:
                min_x = x_sensor - d
            if x_sensor + d > max_x:
                max_x = x_sensor + d

    print(min_x, max_x)


    count = 0
    points = []
    new_sensors = sensors.copy()
    for i, s in enumerate(sensors):
        new_sensors.remove(s)
        for ss in new_sensors:
            if ss is s:
                print("same")
                continue

            d = compute_distance(s.position, ss.position)
            if d >= s.distance + ss.distance + 2:
                print()
                print(s.position, s.distance)
                print(ss.position, ss.distance)
                ddo = d - s.distance - ss.distance
                for dd in range(math.floor(ddo/2), math.ceil(ddo/2) + 1):
                    dx = ss.x - s.x
                    dy = ss.y - s.y
                    print(dx, dy)
                    proportion = (s.distance + round(dd)) / d
                    print(proportion)
                    dx = dx * proportion
                    dy = dy * proportion
                    print(dx, dy)
                    dx = math.ceil(dx) if dx >= 0 else math.floor(dx)
                    dy = math.ceil(dy) if dy >= 0 else math.floor(dy)
                    print(dx, dy)
                    x = s.x + dx
                    y = s.y + dy
                    print(x, y)
                    dtest = compute_distance(s.position, (x,y))
                    print(s.distance, dtest)
                    if not dtest > s.distance:
                        continue
                    dtest = compute_distance(ss.position, (x, y))
                    print(ss.distance, dtest)
                    if not dtest > ss.distance:
                        continue

                    for sensor in sensors:
                        if (x, y) == sensor.position:
                            continue
                    if (x,y) in points:
                        print("FOUND")
                        print(x,y)
                        count += 1
                        #return x * 4000000 + y
                    else:
                        points.append((x,y))
        print(points)

    print(count)
    for point in points:
        found = True
        for s in sensors:
            d = compute_distance(s.position, point)
            if d <= s.distance:
                found = False
                break
        if found:
            x = point[0]
            y = point[1]
            print("FOUND")
            print(x, y)
            return x * 4000000 + y


    return 0

def test():
    res = 0
    length = 4000001
    # length = 21
    beacons = []
    sensors = []
    min_x = 1000000
    max_x = 0
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            x_sensor, y_sensor, x_beacon, y_beacon = [int(s) for s in re.findall(r'[-+]?\b\d+\b', line_stripped)]
            # print(x_sensor, y_sensor, x_beacon, y_beacon)
            d = compute_distance((x_sensor, y_sensor), (x_beacon, y_beacon))
            sensors.append(Sensor(x_sensor, y_sensor, d))
            beacons.append((x_beacon, y_beacon))
            # print(d)
            if x_sensor - d < min_x:
                min_x = x_sensor - d
            if x_sensor + d > max_x:
                max_x = x_sensor + d

    print(min_x, max_x)

    for x in range(2300000, 2310000):
        for y in range(2990000, 2995000):
            found = True
            for s in sensors:
                d = compute_distance(s.position, (x, y))
                if d <= s.distance:
                    found = False
                    break
            if found:
                print("FOUND")
                print(x, y)
                return x * 4000000 + y



def main():
    #print("Test: ", test())
    res_a = a()
    print("a: " + str(res_a))
    res_b = b()
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
