# https://adventofcode.com/2025/day/2#part2

import re

with open("input.txt") as f:
    id_ranges = f.read().split(",")

invalid_ids = []
for id_range in id_ranges:
    start, stop = map(int, id_range.split("-"))
    id_range = list(map(str, range(start, stop + 1)))

    [invalid_ids.append(int(id)) for id in id_range if re.match(r"^(\d+)\1+$", id)]

print(sum(invalid_ids))
