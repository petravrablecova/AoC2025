# https://adventofcode.com/2025/day/1#part2

no_of_zero_clicks = 0
point = 50

with open('input.txt') as f:
    rotations = f.read().splitlines()

rotations = list(map(lambda x: int(x.replace('L','-').replace('R','+')), rotations))

for rotation in rotations:
    step = rotation // abs(rotation)
    points = list(map(lambda x: x % 100, range(point+step,point+rotation+step, step)))
    no_of_zero_clicks += points.count(0)
    point = (point + rotation) % 100

print(no_of_zero_clicks)