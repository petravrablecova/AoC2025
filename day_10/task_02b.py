# https://adventofcode.com/2025/day/10#part2
# works with sample input only
import functools
from itertools import product


@functools.cache
def push(initial, no_of_pushes, buttons):
    push = list(initial)
    for i, p in enumerate(no_of_pushes):
        for _ in range(p):
            for b in buttons[i]:
                push[b] += 1
    return tuple(push)


available_buttons = []
joltages = []
with open("input0.txt") as f:
    manual = f.read().splitlines()

for line in manual:
    splits = line.split()
    available_buttons.append(splits[1:-1])
    joltages.append(splits[-1])
del splits, line, manual, f

joltages = list(map(lambda x: tuple(eval(x.replace("{", "[").replace("}", "]"))), joltages))
available_buttons = [
    eval("[" + ",".join(buttons).replace("(", "[").replace(")", "]") + "]") for buttons in available_buttons
]
available_buttons = [list(map(tuple, ab)) for ab in available_buttons]

minimum_pushes = []
for joltage, buttons in zip(joltages, available_buttons):

    initial_joltage = tuple([0] * len(joltage))

    button_combos = list(product(*[range(max(joltage) + 1)] * len(buttons)))
    button_combos.sort(key=lambda x: sum(x))
    for combo in button_combos:
        if push(initial_joltage, combo, tuple(buttons)) == joltage:
            minimum_pushes.append(combo)
            break

print(sum([sum(minimum) for minimum in minimum_pushes]))
