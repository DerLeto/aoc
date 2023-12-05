import numpy as np

input_path = "input/9.txt"

dirs = {"R": (1,0), "L": (-1,0), "U": (0,1), "D": (0,-1)}

def a():
    res = 1
    head_pos = [0, 0]
    tail_pos = [0, 0]
    visited = [(0,0)]
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            direction, steps = line_stripped.split()

            if direction == "R":
                for i in range(int(steps)):
                    head_pos[0] += 1
                    if head_pos[0] > tail_pos[0] + 1:
                        tail_pos[0] += 1
                        tail_pos[1] = head_pos[1]
                        if (tail_pos[0], tail_pos[1]) not in visited:
                            visited.append((tail_pos[0], tail_pos[1]))
                            res += 1
            elif direction == "L":
                for i in range(int(steps)):
                    head_pos[0] -= 1
                    if head_pos[0] < tail_pos[0] - 1:
                        tail_pos[0] -= 1
                        tail_pos[1] = head_pos[1]
                        if (tail_pos[0], tail_pos[1]) not in visited:
                            visited.append((tail_pos[0], tail_pos[1]))
                            res += 1
            elif direction == "U":
                for i in range(int(steps)):
                    head_pos[1] += 1
                    if head_pos[1] > tail_pos[1] + 1:
                        tail_pos[1] += 1
                        tail_pos[0] = head_pos[0]
                        if (tail_pos[0], tail_pos[1]) not in visited:
                            visited.append((tail_pos[0], tail_pos[1]))
                            res += 1
            elif direction == "D":
                for i in range(int(steps)):
                    head_pos[1] -= 1
                    if head_pos[1] < tail_pos[1] - 1:
                        tail_pos[1] -= 1
                        tail_pos[0] = head_pos[0]
                        if (tail_pos[0], tail_pos[1]) not in visited:
                            visited.append((tail_pos[0], tail_pos[1]))
                            res += 1

    return res


def b():
    OFFSET = 100000
    res = 1
    head_pos = (OFFSET, OFFSET)
    poses = [(OFFSET,OFFSET) for i in range(8)]
    tail_pos = (OFFSET, OFFSET)
    visited = [(OFFSET, OFFSET)]
    # visualize(head_pos, poses, tail_pos, 6, 5)
    with open(input_path) as file:
        for line in file:
            line_stripped = line.strip()
            # print("=== ", line_stripped, " ===")
            dir, steps = line_stripped.split()
            vector = dirs[dir]
            for i in range(int(steps)):
                head_pos = (head_pos[0] + vector[0], head_pos[1] + vector[1])
                print(head_pos)
                ref = head_pos
                new_poses = []
                for pose in poses:
                    new_pose = move_part(ref, pose)
                    new_poses.append(new_pose)
                    ref = new_pose
                poses = new_poses
                tail_pos = move_part(ref, tail_pos)
                if tail_pos not in visited:
                    visited.append(tail_pos)
                    res += 1
                # visualize(head_pos, poses, tail_pos, 6, 5)


    return res

def move_part(ref, part):
    dx = ref[0] - part[0]
    dy = ref[1] - part[1]

    if abs(dx) <= 1 and abs(dy) <=1:
        return part

    if abs(dx) > abs(dy):
        y = ref[1]
        if dx > 0:
            return part[0] + dx - 1, y
        else:
            return part[0] + dx + 1, y
    elif abs(dx) < abs(dy):
        x = ref[0]
        if dy > 0:
            return x, part[1] + dy - 1
        else:
            return x, part[1] + dy + 1
    else:
        if dx > 0:
            x = part[0] + dx - 1
        else:
            x = part[0] + dx + 1

        if dy > 0:
            y = part[1] + dy - 1
        else:
            y = part[1] + dy + 1

        return x, y


def visualize(head_pose, poses, tail_pose, wx, wy):
    array = np.zeros(shape=(wx,wy), dtype=int)
    for i, pose in enumerate(poses):
        array[pose] = i + 2
    array[tail_pose] = 10
    array[head_pose] = 1
    print(np.fliplr(array).transpose())




def main():
    res_a = a()
    res_b = b()
    print("a: " + str(res_a))
    print("b: " + str(res_b))


if __name__ == "__main__":
    main()
