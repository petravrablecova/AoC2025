# https://adventofcode.com/2025/day/10
import functools
from itertools import combinations
from operator import add


@functools.cache
def push(initial, pushed_buttons):
    push = [False] * len(initial)
    for button in pushed_buttons:
        for b in button:
            push[b] = not push[b]
    push = tuple(map(lambda x: -11 if x else 0, push))

    return tuple(map(add, initial, push))


indicators = []
available_buttons = []
joltages = []
with open("input0.txt") as f:
    manual = f.read().splitlines()

for line in manual:
    splits = line.split()
    indicators.append(splits[0][1:-1])
    available_buttons.append(splits[1:-1])
del splits, line, manual, f

available_buttons = [
    eval("[" + ",".join(buttons).replace("(", "[").replace(")", "]") + "]") for buttons in available_buttons
]
available_buttons = [list(map(tuple, ab)) for ab in available_buttons]
indicators = [tuple(map(ord, indicator)) for indicator in indicators]

minimum_pushes = []
for indicator, buttons in zip(indicators, available_buttons):
    initial_indicator = tuple([46] * len(indicator))
    found_r = False
    for r in range(1, len(indicator) + 1):
        button_combos = combinations(buttons, r)
        for combo in button_combos:
            if push(initial_indicator, combo) == indicator:
                minimum_pushes.append(r)
                found_r = True
                break
        if found_r:
            break

print(sum(minimum_pushes))
