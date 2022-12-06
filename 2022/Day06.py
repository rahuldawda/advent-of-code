def solve(data, unique):
    for i in range(unique, len(data)):
        if len(set(data[i-unique:i])) == unique:
            return i

data = open("D:\\AoC\\2022\\day06.txt", "r").read().splitlines()
print(solve(data[0], unique = 4))
print(solve(data[0], unique = 14))