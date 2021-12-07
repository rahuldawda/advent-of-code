from collections import *
import statistics

def part1(input):
    average = int(statistics.median(input))
    fuel = 0
    for crab in input:
        fuel += abs(crab - average)
    return fuel

def part2(input):
    fuel = 0
    average = int(statistics.mean(input))
    for crab in input:
        fuel += sum(range(abs(crab - average) + 1))
    return fuel

data = open("day7.txt", "r").read().split(",")
input = [int(x) for x in data]
print(part1(input))
print(part2(input))