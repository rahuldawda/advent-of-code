from collections import *

def part1(input):
    count = 0
    for i in range(len(input)):
        if input[i-1] < input[i]:
            count += 1
    return count

def part2(input):
    count = 0
    for i in range(len(input)):
        if i >= 3 and input[i-1] + input[i-2] + input[i-3] < input[i] + input[i-1] + input[i-2]:
            count += 1
    return count

data = open("day1.txt", "r").read().splitlines()
input = [int(x) for x in data]
print(part1(input))
print(part2(input))