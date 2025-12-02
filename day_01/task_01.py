# https://adventofcode.com/2025/day/1

no_of_zero_landings = 0
point = 50

with open("input.txt") as f:
    rotations = f.read().splitlines()

rotations = list(map(lambda x: int(x.replace("L", "-").replace("R", "+")), rotations))

for rotation in rotations:
    point = (point + rotation) % 100
    no_of_zero_landings += int(point == 0)

print(no_of_zero_landings)
