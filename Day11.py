import itertools

def neighbors(cell):
    for point in itertools.product(range(-1, 2), repeat=2):
        if point == (0, 0):
            continue
        x = cell[0] + point[0]
        y = cell[1] + point[1]
        if (0 <= x < columns) and (0 <= y < rows):
            yield (x, y)

def calc_flashes(data, rows, columns, count):
    total = 0
    cells = columns * rows    
    for step in itertools.count(1):
        flashes = 0
        # increment energy
        data = [[x + 1 for x in num] for num in data]
        dataset = [(i, j) for i, row in enumerate(data) for j, x in enumerate(row) if x > 9]
        while dataset:
            (i, j) = dataset.pop()
            flashes += 1
            for (i1, j1) in neighbors((i, j)):
                data[i1][j1] += 1
                if data[i1][j1] == 10:
                    dataset.append((i1, j1))
        total += flashes
        if count > 0 and step == count:
            return total
        if flashes == cells:
            return step
        data = [[0 if x > 9 else x for x in row] for row in data]

def part1(input, rows, columns):
    # simulating 100 steps
    return calc_flashes(input, rows, columns, 100)

def part2(input, rows, columns):
    # no count provided, stop when all flash together
    return calc_flashes(input, rows, columns, 0)

data = open("day11.txt", "r").read().splitlines()
rows, columns = len(data), len(data[0]) 
data = [[int(x) for x in num] for num in data]
print(part1(data, rows, columns))
print(part2(data, rows, columns))