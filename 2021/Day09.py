from collections import *
from functools import reduce
import operator

def process_data(input):
    return [[int(x) for x in num] for num in input]

def build_basin(input):
    basin = {}
    for i in range(len(input)):
        for j in range(len(input[0])):
            pt = (i,j)
            n = []
            if i - 1 >= 0 and input[i - 1][j] != 9: n.append((i - 1, j))
            if i + 1 < len(input) and input[i + 1][j] != 9: n.append((i + 1, j))
            if j - 1 >= 0 and input[i][j-1] != 9: n.append((i, j - 1))
            if j + 1 < len(input[0]) and input[i][j + 1] != 9: n.append((i, j + 1))
            basin[pt] = n
    return basin

def part1(input):
    output = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if (i < len(input) - 1 and input[i][j] >= input[i + 1][j]) or \
		    input[i][j] >= input[i - 1][j] or \
            j > 0 and input[i][j] >= input[i][j - 1] or \
            (j < len(input[0]) - 1 and input[i][j] >= input[i][j + 1]):
                continue
            output += input[i][j] + 1
    return output

def part2(input):
    sizes = []
    basin = build_basin(input)
    traversed = set()
    for x in basin.keys():
        if x in traversed:
            continue
        size = 0
        lst = [x]
        while lst:
            node = lst.pop(0)
            for next in basin[node]:
                if next not in traversed:
                    traversed.add(next)
                    lst.append(next)
                    size += 1
        sizes.append(size)
    sorted_sizes = sorted(sizes)[::-1][:3]
    return reduce(operator.mul, (sorted_sizes))

data = process_data(open("day9.txt", "r").read().splitlines())
print(part1(data))
print(part2(data))