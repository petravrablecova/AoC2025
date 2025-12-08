# https://adventofcode.com/2025/day/7#part2
import functools

with open("input.txt") as f:
    manifold = f.read().splitlines()

start = manifold[0].index("S")
beam_path = [start]
for row in range(1, len(manifold)):
    new_beam_path = []
    for beam in beam_path:
        match manifold[row][beam]:
            case ".":
                new_beam_path.append(beam)
                manifold[row] = manifold[row][:beam] + "|" + manifold[row][beam + 1 :]
                continue
            case "^":
                if beam - 1 >= 0:
                    if "." == manifold[row][beam - 1]:
                        new_beam_path.append(beam - 1)
                        manifold[row] = manifold[row][: beam - 1] + "|" + manifold[row][beam:]
                if beam + 1 < len(manifold[row]):
                    if "." == manifold[row][beam + 1]:
                        new_beam_path.append(beam + 1)
                        manifold[row] = manifold[row][: beam + 1] + "|" + manifold[row][beam + 2 :]
    beam_path = new_beam_path


@functools.cache
def children(row, column):
    if all([manifold[i][column] == "|" for i in range(row + 1, len(manifold))]):
        return []
    else:
        next_split_row = "".join([manifold[i][column] for i in range(row + 1, len(manifold))]).index("^")
        next_split_row += row + 1
        children_nodes = []
        if column - 1 >= 0:
            children_nodes.append((next_split_row, column - 1))
        if column + 1 < len(manifold[row]):
            children_nodes.append((next_split_row, column + 1))
        return children_nodes


@functools.cache
def paths(row, column):
    childs = children(row, column)
    if len(childs) == 0:
        return 1
    else:
        return sum([paths(*child) for child in childs])


print(paths(0, start))
