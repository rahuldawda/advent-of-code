import collections

def split_data(data):
    ones = []
    twos = []
    counter = 0
    for line in data:
        split_data = line.split(" -> ")
        ones.append([int(x) for x in split_data[0].split(",")])
        twos.append([int(x) for x in split_data[1].split(",")])
    return ones, twos

def result(touched):
    count = 0

    for value in touched.values():
        if value > 1:
            count += 1
    return count

def part1(ones, twos):
    touched = collections.defaultdict(int)
    for i in range(len(ones)):
        x0, y0 = ones[i]
        x1, y1 = twos[i]

        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                touched[(x0, y)] += 1
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                touched[(x, y0)] += 1
    
    return touched
    

def part2(ones, twos):
    touched = collections.defaultdict(int)
    for i in range(len(ones)):
        x0, y0 = ones[i]
        x1, y1 = twos[i]
        dx = x1 - x0
        dy = y1 - y0
        for i in range(1+max(abs(dx), abs(dy))):
            if dx > 0:
                x = x0 + i
            elif dx < 0:
                x = x0 - i
            else:
                x = x0

            if dy > 0:
                y = y0 + i
            elif dy < 0:
                y = y0 - i
            else:
                y = y0
            touched[(x, y)] += 1

    return touched

data = open("day5.txt", "r").read().splitlines()
ones, twos = split_data(data)
print(result(part1(ones, twos)))
print(result(part2(ones, twos)))