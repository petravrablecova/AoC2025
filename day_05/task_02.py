# https://adventofcode.com/2025/day/5#part2

with open("input.txt") as f:
    db = f.read().splitlines()

id_ranges = db[: db.index("")]
id_ranges = list(map(lambda x: list(map(int, x.split("-"))), id_ranges))
id_ranges = sorted(id_ranges, key=lambda x: (x[0], x[1]))

to_pop = []
for i, id_range in enumerate(id_ranges):
    if i == 0:
        previous = id_range
        continue
    if previous[1] >= id_range[0]:
        id_range[0] = min(id_range[1], previous[1] + 1)
        if id_range[0] == id_range[1]:
            to_pop.append(i)
            continue
    previous = id_range
for i in reversed(to_pop):
    id_ranges.pop(i)

print(sum(map(lambda x: len(range(x[0], x[1] + 1)), id_ranges)))
