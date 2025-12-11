# https://adventofcode.com/2025/day/11

with open("input.txt") as f:
    devices = f.read().splitlines()

import networkx as nx

G = nx.DiGraph()
for device in devices:
    from_d, to_d = device.split(":")
    to_d = to_d.strip().split()
    # Add edges to the graph

    G.add_edges_from([(from_d, d) for d in to_d])

paths = list(nx.all_simple_paths(G, source="you", target="out"))
print(len(paths))
