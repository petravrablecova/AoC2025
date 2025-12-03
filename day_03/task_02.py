# https://adventofcode.com/2025/day/3#part2

with open("input.txt") as f:
    banks = f.read().splitlines()

joltages = []
max_no_of_batteries = 12
for bank in banks:
    joltage = ""
    for i in range(max_no_of_batteries - 1, 0, -1):
        max_bat = max(bank[:-i])
        bank = bank[bank.index(max_bat) + 1 :]
        joltage += max_bat
    max_bat = max(bank)
    joltage += max_bat
    joltages.append(int(joltage))

print(sum(joltages))
