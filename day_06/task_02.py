# https://adventofcode.com/2025/day/6#part2

with open("input.txt") as f:
    raw_math = f.read().splitlines()

math = list(map(str.split, raw_math))

total = 0
for column in range(len(math[0])):
    max_length = max(map(len, [math[row][column] for row in range(len(math))]))
    raw_problem = [line[:max_length].rjust(max_length) for line in raw_math]
    raw_math = [line[max_length + 1 :] for line in raw_math]
    numbers = ["".join([raw_problem[i][j] for i in range(len(raw_problem) - 1)]) for j in range(max_length)]
    total += eval(raw_problem[-1].join(numbers))

print(total)
