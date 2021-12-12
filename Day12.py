from collections import *

def count_paths(vertices, flag):
    start = ('start', set(['start']), None)
    count = 0
    # https://www.geeksforgeeks.org/deque-in-python/
    vertex = deque([start])
    while vertex:
        pos, small, twice = vertex.popleft()
        if pos == 'end':
            count += 1
            continue
        for v in vertices[pos]:
            if v not in small:
                new_small = set(small)
                if v.lower() == v:
                    new_small.add(v)
                vertex.append((v, new_small, twice))
            elif v in small and twice is None and v not in ['start', 'end'] and not flag:
                vertex.append((v, small, v))
    return count

data = open("day12.txt", "r").read().splitlines()
vertices = defaultdict(list)
for line in data:
    x,y = line.strip().split('-')
    vertices[x].append(y)
    vertices[y].append(x)

print(count_paths(vertices, True))
print(count_paths(vertices, False))