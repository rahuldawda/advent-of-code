def part1(data):
    return sum(a1 <= b1 and b2 <= a2 or b1 <= a1 and a2 <= b2 for a1, a2, b1, b2 in data)

def part2(data):
    return  sum(b1 <= a1 <= b2 or a1 <= b1 <= a2 for a1, a2, b1, b2 in data)

data = [tuple(int(x) for assignment in row.split(',') for x in assignment.split('-')) for row in open("D:\\AoC\\2022\\day04.txt", "r").read().splitlines()]
print(part1(data))
print(part2(data))