from collections import defaultdict

def parse_directories(data):
    dirs = defaultdict(int)
    path = []
    for line in data:
        parts = line.split(' ')
        if parts[0] == 'dir':
            continue
        elif parts[1] == 'cd':
            if parts[2] == '..':
                path.pop()
            else:
                path.append(parts[2])
        elif parts[1] == 'ls':
            continue
        else:
            dir = int(parts[0])
            for i in range(1, len(path)+1):
                dirs['/'.join(path[:i])] += dir

    return dirs

def part1(dirs):
    total = 0
    for key in dirs:
        if dirs[key] <= 100000:
            total += dirs[key]
    return total

def part2(dirs):
    total = 1000000000000
    used = dirs['/']
    max_size = 70000000 - 30000000
    remove = used - max_size
    for key in dirs:
        if dirs[key] >= remove:
            total = min(total, dirs[key])
    return total

data = open("D:\\AoC\\2022\\day07.txt", "r").read().splitlines()
dirs = parse_directories(data)
print(part1(dirs))
print(part2(dirs))