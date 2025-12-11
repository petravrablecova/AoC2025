# https://adventofcode.com/2025/day/11#part2

with open("input.txt") as f:
    devices = f.read().splitlines()

import networkx as nx

G = nx.DiGraph()
for device in devices:
    from_d, to_d = device.split(":")
    to_d = to_d.strip().split()
    G.add_edges_from([(from_d, d) for d in to_d])


def count_paths(graph, start, end):
    order = list(nx.topological_sort(G))

    no_of_paths = {node: 0 for node in G}
    no_of_paths[start] = 1

    for u in order:
        for v in graph.successors(u):
            no_of_paths[v] += no_of_paths[u]

    return no_of_paths[end]


# Segment path counts
paths_svr_fft = count_paths(G, "svr", "fft")
paths_fft_dac = count_paths(G, "fft", "dac")
paths_dac_out = count_paths(G, "dac", "out")
paths_svr_fft_dac_out = paths_svr_fft * paths_fft_dac * paths_dac_out

paths_svr_dac = count_paths(G, "svr", "dac")
paths_dac_fft = count_paths(G, "dac", "fft")
paths_fft_out = count_paths(G, "fft", "out")
paths_svr_dac_fft_out = paths_svr_dac * paths_dac_fft * paths_fft_out

print(paths_svr_fft_dac_out + paths_svr_dac_fft_out)
