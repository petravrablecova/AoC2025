# https://adventofcode.com/2025/day/5

with open("input0.txt") as f:
    db = f.read().splitlines()

id_ranges = sorted(db[: db.index("")])
available_ids = list(map(int, db[db.index("") + 1 :]))

id_ranges = list(map(lambda x: list(map(int, x.split("-"))), id_ranges))

fresh_available_ids = []
for id in available_ids:
    relevant_ranges = list(filter(lambda x: x[0] <= id <= x[1], id_ranges))
    if len(relevant_ranges) > 0:
        fresh_available_ids.append(id)

print(len(fresh_available_ids))
