import numpy as np
from graph import get_utility_sequence
from config import INFINITY
from visuals import draw_utility_sequence

number_nodes = 3
graph = [[(-np.inf, -np.inf) for x in range(number_nodes)] for y in range(number_nodes)]

graph[0][1] = (5, -1)
graph[1][0] = (5, -1)
graph[0][2] = (-1, 1)
graph[2][2] = (-1, 1)


def get_path():
    path = []
    path.append((0, 1))
    path.append((1, 0))
    path.append((0, 2))
    for _ in range(INFINITY):
        path.append((2, 2))
    return path


T = 6
path = get_path()
utility = get_utility_sequence(graph, path)
draw_utility_sequence(utility, T)
