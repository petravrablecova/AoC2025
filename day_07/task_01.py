# https://adventofcode.com/2025/day/7

with open("input0.txt") as f:
    manifold = f.read().splitlines()

start = manifold[0].index("S")
beam_path = [start]
for row in range(1, len(manifold)):
    new_beam_path = []
    for beam in beam_path:
        match manifold[row][beam]:
            case ".":
                new_beam_path.append(beam)
                manifold[row] = manifold[row][:beam] + "|" + manifold[row][beam + 1 :]
                continue
            case "^":
                if beam - 1 >= 0:
                    if "." == manifold[row][beam - 1]:
                        new_beam_path.append(beam - 1)
                        manifold[row] = manifold[row][: beam - 1] + "|" + manifold[row][beam:]
                if beam + 1 < len(manifold[row]):
                    if "." == manifold[row][beam + 1]:
                        new_beam_path.append(beam + 1)
                        manifold[row] = manifold[row][: beam + 1] + "|" + manifold[row][beam + 2 :]
    beam_path = new_beam_path


splitters = [
    (row, column) for row in range(len(manifold)) for column in range(len(manifold[0])) if "^" == manifold[row][column]
]
activated_splitters = [splitter for splitter in splitters if "|" == manifold[splitter[0] - 1][splitter[1]]]

print(len(activated_splitters))
