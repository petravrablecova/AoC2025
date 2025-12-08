# https://adventofcode.com/2025/day/8
import collections
import functools
import itertools
from functools import reduce
import operator
import numpy as np

with open("input.txt") as f:
    junction_boxes = f.read().splitlines()

MAX_CONNECTIONS = 1000


@functools.cache
def distance(box1, box2):
    return pow(box1[0] - box2[0], 2) + pow(box1[1] - box2[1], 2) + pow(box1[2] - box2[2], 2)


junction_boxes = list(map(lambda x: tuple(map(int, x.split(","))), junction_boxes))
junction_boxes = sorted(junction_boxes)
distances = [[np.inf for _ in range(len(junction_boxes))] for _ in range(len(junction_boxes))]

for i, box1 in enumerate(junction_boxes):
    for j in range(i + 1, len(junction_boxes)):
        distances[i][j] = distance(box1, junction_boxes[j])

distances_list = list(itertools.chain(*distances))
min_indices = sorted(range(len(distances_list)), key=distances_list.__getitem__)
min_indices = [(i % len(junction_boxes), i // len(junction_boxes)) for i in min_indices]

circuits = {}
no_of_made_connections = 0
for i, connection in enumerate(min_indices):
    if no_of_made_connections == MAX_CONNECTIONS:
        break
    circuit0 = circuits[connection[0]] if connection[0] in circuits else False
    circuit1 = circuits[connection[1]] if connection[1] in circuits else False

    if not circuit0 and not circuit1:
        circuits[connection[0]] = i
        circuits[connection[1]] = i
    if circuit0 and not circuit1:
        circuits[connection[1]] = circuit0
    if circuit1 and not circuit0:
        circuits[connection[0]] = circuit1
    if circuit0 and circuit1:
        for k, c in circuits.items():
            circuits[k] = circuit1 if c == circuit0 else c
    no_of_made_connections += 1


biggest_circuits = [l for c, l in collections.Counter(circuits.values()).most_common(3)]

print(reduce(operator.mul, biggest_circuits, 1))
