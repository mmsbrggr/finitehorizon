import numpy as np
from graph import get_utility_sequence
from adversary import get_optimal_path_info
from config import INFINITY
from visuals import draw_utility_sequence

number_nodes = 6
graph = np.full((number_nodes, number_nodes), -np.inf)
graph[0, 1] = 0
graph[0, 5] = 1
graph[1, 2] = 1
graph[2, 0] = 1
graph[2, 3] = 2
graph[2, 4] = 10
graph[3, 3] = 10
graph[4, 4] = 2
graph[5, 5] = 30


def get_path(i):
    path = []
    if i == 1:
        path.append((0, 1))
        path.append((1, 2))
        path.append((2, 3))
        for i in range(INFINITY):
            path.append((3, 3))
    if i == 2:
        path.append((0, 1))
        path.append((1, 2))
        path.append((2, 4))
        for i in range(INFINITY):
            path.append((4, 4))
    if i == 3:
        path.append((0, 1))
        path.append((1, 2))
        path.append((2, 0))
        path.append((0, 5))
        for i in range(INFINITY):
            path.append((5, 5))
    return path


T = 3

path = get_path(3)
u = get_utility_sequence(graph, path)

print("Optimal value of drawn path:")
print(get_optimal_path_info(u, T))

draw_utility_sequence(u, T)
