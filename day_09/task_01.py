# https://adventofcode.com/2025/day/9
import functools
import itertools

with open("input.txt") as f:
    corners = f.read().splitlines()


@functools.cache
def area(corner1, corner2):
    return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)


corners = list(map(lambda x: tuple(map(int, x.split(","))), corners))
corners = sorted(corners)

# calculate largest area
largest_area = 0
for i, corner in enumerate(corners):
    for j in range(i + 1, len(corners)):
        largest_area = max(largest_area, area(corner, corners[j]))

print(largest_area)
