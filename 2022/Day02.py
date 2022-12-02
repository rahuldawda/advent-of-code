def part1(data):
    score_map = {
        'A X': 1 + 3,
        'A Y': 2 + 6,
        'A Z': 3 + 0,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 1 + 6,
        'C Y': 2 + 0,
        'C Z': 3 + 3,
    }
    sum = 0
    for round in data:
        sum += score_map[round]
    return sum

def part2(data):
    score_map = {
        'A X': 3 + 0,
        'A Y': 1 + 3,
        'A Z': 2 + 6,
        'B X': 1 + 0,
        'B Y': 2 + 3,
        'B Z': 3 + 6,
        'C X': 2 + 0,
        'C Y': 3 + 3,
        'C Z': 1 + 6,
    }
    sum = 0
    for round in data:
        sum += score_map[round]
    return sum

data = open("D:\day2.txt", "r").read().splitlines()
print(part1(data))
print(part2(data))