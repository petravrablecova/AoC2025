# https://adventofcode.com/2025/day/3

no_of_zero_landings = 0
point = 50

with open("input.txt") as f:
    banks = f.read().splitlines()

joltages = []
for bank in banks:
    max_bat = max(bank[:-1])
    joltage = max_bat + max(bank[bank.index(max_bat) + 1 :])
    joltages.append(int(joltage))

print(sum(joltages))
