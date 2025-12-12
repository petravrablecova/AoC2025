# https://adventofcode.com/2025/day/12
import functools
import re

from polyomino.constant import MONOMINO
from polyomino.tileset import Tileset
from polyomino.board import Rectangle

with open("input.txt") as f:
    presents_and_regions = f.read()

presents = re.match(r"^(\d+:\n[\.#\n]+\n)+", presents_and_regions).group(0)
regions = presents_and_regions[len(presents) :]
presents = presents.split("\n\n")[:-1]
regions = regions.split("\n")[:-1]

region_sizes = []
no_of_presents = []
for region in regions:
    region_size, no_of_present = region.split(": ")
    region_sizes.append(tuple(sorted(map(int, region_size.split("x")), reverse=True)))
    no_of_presents.append(tuple(map(int, no_of_present.split())))

present_list = []
for present in presents:
    present_coords = []
    for i, line in enumerate(present.split("\n")[1:]):
        for j, char in enumerate(line):
            if char == "#":
                present_coords.append((i, j))
    present_list.append(present_coords)

present_sizes = [sum(c == "#" for c in present) for present in presents]


@functools.cache
def solve(region_size, presents_count):
    global present_list
    presents = []
    for present, count in zip(present_list, presents_count):
        for _ in range(count):
            presents.append(present)
    try:
        board = (
            Rectangle(*region_size).tile_with_set(Tileset(presents, [], [MONOMINO], reflections=True)).with_heuristics()
        )
        solution = board.solve()
        return 1 if solution else 0
    except:
        return 0


no_of_fittable_regions = 0

for region_size, presents_count in zip(region_sizes, no_of_presents):
    if (region_size[0] * region_size[1]) < sum(
        [present * count for present, count in zip(present_sizes, presents_count)]
    ):
        # unsolvable
        continue
    if (region_size[0] - region_size[0] % 3) * (region_size[1] - region_size[1] % 3) >= sum(presents_count) * 9:
        # trivially solvable
        no_of_fittable_regions += 1
    else:
        # rest
        no_of_fittable_regions += solve(region_size, presents_count)

print(no_of_fittable_regions)
