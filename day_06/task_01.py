# https://adventofcode.com/2025/day/6

with open("input.txt") as f:
    math = f.read().splitlines()

math = list(map(str.split, math))

total = 0
for column in range(len(math[0])):
    total += eval(math[-1][column].join([math[row][column] for row in range(len(math) - 1)]))

print(total)
