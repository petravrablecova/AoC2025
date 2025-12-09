# https://adventofcode.com/2025/day/9#part2
import functools


@functools.cache
def corners_and_lines_lies_inside_rectangle(corner1, corner2):
    global corners_and_lines
    min_tile = (min(corner1[0], corner2[0]), min(corner1[1], corner2[1]))
    max_tile = (max(corner1[0], corner2[0]), max(corner1[1], corner2[1]))

    for tile in corners_and_lines:
        if min_tile[0] < tile[0] < max_tile[0] and min_tile[1] < tile[1] < max_tile[1]:
            return True
    return False


@functools.cache
def area(corner1, corner2):
    global largest_area
    if (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1) < largest_area:
        return 0

    if corners_and_lines_lies_inside_rectangle(corner1, corner2):
        return 0

    return (abs(corner1[0] - corner2[0]) + 1) * (abs(corner1[1] - corner2[1]) + 1)


with open("input.txt") as f:
    corners = f.read().splitlines()

corners = list(map(lambda x: tuple(map(int, x.split(","))), corners))
corners = sorted(corners, key=lambda x: (x[1], x[0]))

# add vertical and horizontal lines to get the whole perimeter
lines = []
corners_rows = list(map(lambda x: x[0], corners))
for i in range(min(corners_rows), max(corners_rows) + 1):
    row_corners = [c for c in corners if c[0] == i]
    for index, corner in enumerate(row_corners):
        if index % 2 == 0:  # 0x1 2x3 4x5 6x7
            for j in range(corner[1] + 1, row_corners[index + 1][1]):
                lines.append((i, j))
del corners_rows

corners_columns = list(map(lambda x: x[1], corners))
for i in range(min(corners_columns), max(corners_columns) + 1):
    column_corners = [c for c in corners if c[1] == i]
    for index, corner in enumerate(column_corners):
        if index % 2 == 0:
            for j in range(corner[0] + 1, column_corners[index + 1][0]):
                lines.append((j, i))
del corners_columns

corners_and_lines = sorted(corners + lines)
del lines

# calculate largest area
largest_area = 0
for i, corner in enumerate(corners):
    for j in range(i + 1, len(corners)):
        largest_area = max(largest_area, area(corner, corners[j]))

print(largest_area)
