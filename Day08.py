from collections import *
import itertools

def trans(displays, options, good):
    out = 0
    for d in displays.split():
        t = [options[s] for s in d]
        digit = good.index(set(t))
        out = 10*out + digit
    return out

def part1(input):
    count = 0
    for line in input:
        patterns = line.split('|')[1].split()
        for thing in patterns:
            if len(thing) in [2, 4, 3, 7]:
                count += 1
    return count

def part2(input):
    *good, = map(set, ['abcefg','cf','acdeg','acdfg','bcdf','abdfg','abdefg','acf','abcdefg','abcdfg'])

    s = 0
    for x,y in [x.split('|') for x in input]:
      for p in itertools.permutations('abcdefg'):
        options = dict(zip('abcdefg', p))

        try:                                   
            _ = trans(x, options, good)                       
            s += trans(y, options, good)                      
        except ValueError:                     
            pass                               
    print(s)

data = open("day8.txt", "r").read().splitlines()
print(part1(data))
print(part2(data))