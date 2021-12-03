from collections import *

def part1(data):
    gamma = ""
    epsilon = ""
    ones = 0
    zeros = 0
    size = len(data[0])
    for i in range(size):
        ones = 0
        zeros = 0
        for value in data:
            if value[i] == "1":
                ones += 1
            else:
                zeros += 1

        if ones > zeros:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    
    return gamma * epsilon


def part2(data):
    one_list = []
    zero_list = []
    filter_o2_list = data
    filter_co2_list = data
    o2 = co2 = 0
    size = len(data[0])
    for i in range(size):
        ones = 0
        zeros = 0
        for value in data:
            if value in filter_o2_list:
                if value[i] == "1":
                    ones += 1
                else:
                    zeros += 1
        if ones >= zeros:
            filter_o2_list = list(filter(lambda x: x[i] == '1', filter_o2_list))
        else:
            filter_o2_list = list(filter(lambda x: x[i] == '0', filter_o2_list))

        if len(filter_o2_list) == 1:
            o2 = int(filter_o2_list[0], 2)
            break

    for i in range(size):
        ones = 0
        zeros = 0
        for value in data:
            if value in filter_co2_list:
                if value[i] == "1":
                    ones += 1
                else:
                    zeros += 1
        if ones >= zeros:
            filter_co2_list = list(filter(lambda x: x[i] == '0', filter_co2_list))
        else:
            filter_co2_list = list(filter(lambda x: x[i] == '1', filter_co2_list))

        if len(filter_co2_list) == 1:
            co2 = int(filter_co2_list[0], 2)
            break

    return o2 * co2

data = open("day3.txt", "r").read().splitlines()
print(part1(data))
print(part2(data))