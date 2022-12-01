from collections import *

def count_polymers(input, rules, iterations):
    counter = Counter()
    for i in range(len(input)-1):
        counter[input[i]+input[i+1]] += 1

    for iter in range(iterations+1):
        if iter == iterations:
            internal = Counter()
            for k in counter:
                internal[k[0]] += counter[k]
            print(max(internal.values())-min(internal.values())+1)

        new_counter = Counter()
        for k in counter:
            new_counter[k[0]+rules[k]] += counter[k]
            new_counter[rules[k]+k[1]] += counter[k]
        counter = new_counter

data, conditions = open("day14.txt", "r").read().split('\n\n')
rules = {}
for line in conditions.strip().split('\n'):
    polymer,insert = line.strip().split(' -> ')
    rules[polymer] = insert

print(count_polymers(data, rules, 10))
print(count_polymers(data, rules, 40))