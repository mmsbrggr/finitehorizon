import numpy as np
from graph import get_utility_sequence
from adversary import get_optimal_path_info
from config import INFINITY
from visuals import draw_utility_sequence

number_nodes = 4
graph = np.full((number_nodes, number_nodes), -np.inf)
graph[0, 1] = -1
graph[0, 2] = 2
graph[0, 3] = 5
graph[1, 0] = -1
graph[2, 0] = 2
graph[3, 3] = 5


def get_path(i):
    path = []
    for _ in range(i):
        path.append((0, 2))
        path.append((2, 0))
    path.append((0, 1))
    path.append((1, 0))
    path.append((0, 3))
    for _ in range(INFINITY):
        path.append((3, 3))
    return path


T = 10

path = get_path(3)
u = get_utility_sequence(graph, path)
draw_utility_sequence(u, T)

print("Optimal value of drawn path:")
print(get_optimal_path_info(u, T)['value'])
