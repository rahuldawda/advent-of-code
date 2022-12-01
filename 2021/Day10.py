from collections import *

def solve(input):
    scores = []
    total = 0
    for line in input:
        bad = False
        queue = deque()
        for c in line.strip():
            if c in ['(', '[', '{', '<']:
                queue.append(c)
            elif c==')':
                if queue[-1] != '(':
                    total += 3
                    bad = True
                    break
                else:
                    queue.pop()
            elif c==']':
                if queue[-1] != '[':
                    total += 57
                    bad = True
                    break
                else:
                    queue.pop()
            elif c=='}':
                if queue[-1] != '{':
                    total += 1197
                    bad = True
                    break
                else:
                    queue.pop()
            elif c=='>':
                if queue[-1] != '<':
                    total += 25137
                    bad = True
                    break
                else:
                    queue.pop()
        if not bad:
            score = 0
            weight = {'(': 1, '[': 2, '{': 3, '<': 4}
            for c in reversed(queue):
                score = score*5 + weight[c]
            scores.append(score)

    #part 1
    print(total)

    #part 2
    scores.sort()
    print(scores[len(scores)//2])

data = open("day10.txt", "r").read().splitlines()
solve(data)