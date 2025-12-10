# https://adventofcode.com/2025/day/10#part2
from pulp import LpProblem, LpMinimize, LpVariable
import numpy as np
from pulp import GLPK

available_buttons = []
joltages = []
with open("input.txt") as f:
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
for i in range(len(joltages)):
    new_buttons = []
    for button in available_buttons[i]:
        new_button = [0] * len(joltages[i])
        for j in button:
            new_button[j] = 1
        new_buttons.append(new_button)
    available_buttons[i] = new_buttons

# minimize a1 + a2 + ... + an, n=len(buttons)
# a1 * button1 + a2 * button2 + ... + an * buttonn = joltage
sum_of_pushed_buttons = 0
for i, joltage in enumerate(joltages):
    prob = LpProblem("myProblem", LpMinimize)

    # variables
    no_of_pushes = [LpVariable(name=f"a{j}", lowBound=0, cat="Integer") for j in range(len(available_buttons[i]))]
    # constraints
    constraints = np.array(
        [[no_of_pushes[j] * b for b in available_buttons[i][j]] for j in range(len(available_buttons[i]))]
    ).sum(axis=0)
    for k, jolt in enumerate(joltage):
        prob += constraints[k] == jolt
    # objective function
    prob += sum(no_of_pushes)
    status = prob.solve(solver=GLPK(msg=False))
    sum_of_pushed_buttons += prob.objective.value()

print(sum_of_pushed_buttons)
