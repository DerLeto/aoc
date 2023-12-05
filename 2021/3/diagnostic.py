import copy
from sys import argv


def task_1(data_in, bin=False):
    if data_in.__class__ is list:
        data = data_in.copy()
    else:
        data = data_in.split('\n')
    bit_count = 0
    bits = {}
    total_number = 1

    for bit in data[0]:
        bits[bit_count] = int(bit)
        bit_count += 1

    for line in data[1:]:
        total_number += 1
        bit_count = 0
        for bit in line:
            bits[bit_count] += int(bit)
            bit_count += 1

    gamma_rate = ""
    epsilon_rate = ""
    for bit_number, count in bits.items():
        if count >= total_number/2:
            gamma_rate += '1'
            epsilon_rate += '0'
        else:
            gamma_rate += '0'
            epsilon_rate += '1'
    print(gamma_rate)
    print(epsilon_rate)

    if bin:
        return gamma_rate, epsilon_rate
    else:
        return int(gamma_rate, 2), int(epsilon_rate, 2)


def task_2(data_str):
    data_task_2 = data_str.split('\n')

    oxygen = get_parameter(data_task_2, 0)
    life_support = get_parameter(data_task_2, 1)

    print(oxygen)
    print(life_support)
    return int(oxygen, 2), int(life_support, 2)


def get_parameter(data_param, index):
    current_data = data_param.copy()
    remaining_data = []

    for i in range(len(current_data[0])):
        bits = task_1(current_data, True)[index]
        for line in current_data:
            if line[i] == bits[i]:
                remaining_data.append(line)

        if len(remaining_data) == 1:
            parameter = remaining_data[0]
            break
        elif len(remaining_data) == 0:
            parameter = current_data[-1]
            break
        else:
            current_data = remaining_data
            remaining_data = []

    return parameter


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: <path to input>")
        exit(0)

    file = argv[1]
    data = open(file)
    most, least = task_2(data.read())
    print("Most: " + str(most) + " | Least: " + str(least))
    print("Result: " + str(most * least))
