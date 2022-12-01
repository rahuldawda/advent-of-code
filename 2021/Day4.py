from collections import *
import itertools

def split_data(data):
    input, *matrices = data.split("\n\n")
    input = [int(x) for x in input.split(",")]
    counter = 0
    size = len(data)
    bingos = []
    bingo = []
    for matrix in matrices:            
        for line in matrix.strip().split("\n"):
            bingo.append([int(x) for x in line.split()])
        bingos.append(list(bingo))
        bingo = []

    return input, bingos

def scan_data(input, bingos):
    positions = {}
    found = False
    bingo_position = 0
    for bingo in bingos:        
        for i in range(0, len(input) - 1):
            for a, row in enumerate(bingo):
                for j, value in enumerate(row):
                    if value == input[i]:
                        bingo[a][j] = 1000
            # check row
            for line in bingo:
                found = all(x == 1000 for x in line)
                if found:
                    break

            # check column if not found
            if found != True:
                switch_bingo = list(map(list, zip(*bingo)))
                for line in switch_bingo:
                    found = all(x == 1000 for x in line)
                    if found:
                        break

            if found == True:
                bingo_flat = list(itertools.chain(*bingo))
                sum = 0
                for item in bingo_flat:
                    if item != 1000:
                        sum += item
                positions[bingo_position] = [i, sum]
                break
        bingo_position += 1

    return positions
    

def part1(positions):
    smallest_pos = positions[0][0]
    for key in positions:
        if positions[key][0] < smallest_pos:
            smallest_pos = positions[key][0]
            smallest_val = positions[key][1]

    return input[smallest_pos] * smallest_val

    

def part2(positions):
    largest_pos = positions[0][0]
    largest_val = 0
    for key in positions:
        if positions[key][0] > largest_pos:
            largest_pos = positions[key][0]
            largest_val = positions[key][1]

    return input[largest_pos] * largest_val

data = open("day4.txt", "r").read()
input, bingos = split_data(data)
positions = scan_data(input, bingos)
print(part1(positions))
print(part2(positions))