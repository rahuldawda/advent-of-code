from collections import *

def solve(input):
    flag = False
    dots = {}
    for line in input:
        line = line.strip()
        if line and line.startswith('fold'):
            folded_dots = {}
            instr = line.split()[-1]
            d,v = instr.split('=')
            v = int(v)
            if d == 'x':
                for (x,y) in dots:
                    if x < v:
                        folded_dots[(x,y)] = True
                    else:
                        folded_dots[(v-(x-v), y)] = True
            else:
                assert d == 'y'
                for (x,y) in dots:
                    if y < v:
                        folded_dots[(x,y)] = True
                    else:
                        folded_dots[(x, v-(y-v))] = True
            dots = folded_dots
            if not flag:
                flag = True
                # part #1
                print(len(folded_dots))
        elif line:
            x,y = [int(v) for v in line.strip().split(',')]
            dots[(x,y)] = True

    x1 = max([x for x,y in dots.keys()])
    y1 = max([y for x,y in dots.keys()])

    # part #2
    output = ''
    for a in range(y1+1):
        for b in range(x1+1):
            output += ('*' if (b,a) in dots else ' ')
        print(output)
        output = ''

data = open("day13.txt", "r").read().splitlines()
solve(data)