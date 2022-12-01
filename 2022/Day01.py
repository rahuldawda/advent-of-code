output = ([sum(int(line) for line in bunch.split()) for bunch in open("D:\day1.txt", "r").read().split('\n\n')])
print(max(output))
print(sum(sorted(output)[-3:]))
