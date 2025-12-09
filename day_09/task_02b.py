# https://adventofcode.com/2025/day/9#part2
import functools

from shapely import Polygon, box


@functools.cache
def area(corner1, corner2):
    return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)


with open("input.txt") as f:
    corners = f.read().splitlines()
corners = list(map(lambda x: tuple(map(int, x.split(","))), corners))

polygon = Polygon(corners)
largest_area = 0
for i, corner1 in enumerate(corners):
    for j, corner2 in enumerate(corners):
        rect = box(corner1[0], corner1[1], corner2[0], corner2[1])
        if polygon.contains(rect):
            largest_area = max(largest_area, area(corner1, corner2))

print(largest_area)
