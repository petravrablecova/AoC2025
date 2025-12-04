# https://adventofcode.com/2025/day/4


with open("input.txt") as f:
    diagram = f.read().splitlines()

accessible_rolls = 0
for i in range(len(diagram)):
    for j in range(len(diagram[i])):
        if diagram[i][j] == ".":
            continue
        rolls_in_surroundings = [
            "@" == diagram[i - 1][j] if i > 0 else False,
            "@" == diagram[i + 1][j] if i < len(diagram) - 1 else False,
            "@" == diagram[i][j + 1] if j < len(diagram[i]) - 1 else False,
            "@" == diagram[i][j - 1] if j > 0 else False,
            "@" == diagram[i - 1][j - 1] if i > 0 and j > 0 else False,
            "@" == diagram[i - 1][j + 1] if i > 0 and j < len(diagram[i]) - 1 else False,
            "@" == diagram[i + 1][j - 1] if i < len(diagram) - 1 and j > 0 else False,
            "@" == diagram[i + 1][j + 1] if i < len(diagram) - 1 and j < len(diagram[i]) - 1 else False,
        ]
        if sum(rolls_in_surroundings) < 4:
            accessible_rolls += 1

print(accessible_rolls)
