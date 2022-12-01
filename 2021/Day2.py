from collections import *

def part1(data):
    h = 0
    d = 0
    for value in data:
        action, number = value.split()
        if action == "forward":
            h += int(number)
        if action == "up":
            d -= int(number)
        if action == "down":
            d += int(number)

    return h * d

def part2(data):
    h = 0
    d = 0
    a = 0
    for value in data:
        action, number = value.split()
        if action == "forward":
            h += int(number)
            d = d + (int(number) * a)
        if action == "up":
            a -= int(number)
        if action == "down":
            a += int(number)

    return h * d

data = open("day2.txt", "r").read().splitlines()
print(part1(data))
print(part2(data))