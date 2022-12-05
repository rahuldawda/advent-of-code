stacks = [
    ['W','B','D','N','C','F','J'],
    ['P','Z','V','Q','L','S','T'],
    ['P','Z','B','G','J','T'],
    ['D','T','L','J','Z','B','H','C'],
    ['G','V','B','J','S'],
    ['P','S','Q'],
    ['B','V','D','F','L','M','P','N'],
    ['P','S','M','F','B','D','L','R'],
    ['V','D','T','R']
]

def part1(data,cargo):
    for line in data[0].split('\n'):
        size = int(line.split(' ')[1])
        source = int(line.split(' ')[3])
        destination = int(line.split(' ')[5])

        for _ in range(size):
            value = cargo[source-1].pop()
            cargo[destination-1].append(value)

    output = ''
    for x in cargo:
        output += x.pop(~0)

    return output

def part2(data,stacks):
    for line in data[0].split('\n'):
        size = int(line.split(' ')[1])
        source = int(line.split(' ')[3])
        destination = int(line.split(' ')[5])

        values = []
        for _ in range(size):
            value = stacks[source-1].pop()
            values.append(value)
        stacks[destination-1].extend(values[::-1])

    output = ''
    for x in cargo:
        output += x.pop(~0)

    return output

data = open("D:\\AoC\\2022\\day05.txt", "r").read().split('\n\n')[1::]
print(part1(data,stacks.copy()))
print(part2(data,stacks.copy()))