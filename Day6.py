from collections import *

def reproduce_fishes(fishes):
    # https://docs.python.org/3/library/collections.html
    output = Counter()
    for val, count in fishes.items():
        if val > 0:
            output[val - 1] += count
        else:
            output[6] += count
            output[8] += count
    return output

def calculate_fishes(input, iterations):
    numbers = Counter(input)

    for _ in range(iterations):
        numbers = reproduce_fishes(numbers)
    return (sum(numbers.values()))

data = open("day6.txt", "r").read().split(",")
input = [int(x) for x in data]
print(calculate_fishes(input, 80))
print(calculate_fishes(input, 256))