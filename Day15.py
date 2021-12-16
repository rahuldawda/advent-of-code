from collections import *
import heapq
import sys

def calculate_risk(size):
    positions = [[None for _ in range(size*columns)] for _ in range(size*rows)]
    queue = [(0,0,0)]
    while queue:
        # https://docs.python.org/3/library/heapq.html
        (dist,r,c) = heapq.heappop(queue)
        if r<0 or r>=size*rows or c<0 or c>=size*columns:
            continue

        val = input[r%rows][c%columns] + (r//rows) + (c//columns)
        while val > 9:
            val -= 9
        rc_cost = dist + val

        if positions[r][c] is None or rc_cost < positions[r][c]:
            positions[r][c] = rc_cost
        else:
            continue
        if r==size*rows-1 and c==size*columns-1:
            break

        for d in range(4):
            rr = r+row_positions[d]
            cc = c+column_positions[d]
            heapq.heappush(queue, (positions[r][c],rr,cc))
    return positions[size*rows-1][size*columns-1] - input[0][0]

data = open("day15.txt", "r").read().splitlines()
input = []
for line in data:
    input.append([int(x) for x in line.strip()])
rows = len(input)
columns = len(input[0])
row_positions = [-1,0,1,0]
column_positions = [0,1,0,-1]

print(calculate_risk(1))
print(calculate_risk(5))