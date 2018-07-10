import numpy as np
from graph import get_utility_sequence
from config import INFINITY
from visuals import draw_utility_sequence

number_nodes = 4
graph = [[(-np.inf, -np.inf) for x in range(number_nodes)] for y in range(number_nodes)]
a = 4

graph[0][1] = (a, 0)
graph[1][2] = (-1, 1)
graph[2][1] = (0, 0)
graph[1][3] = (a, -a)
graph[3][1] = (0, 0)


def get_path():
    path = [(0, 1)]
    for _ in range(INFINITY // 4):
        for _ in range(a):
            path.append((1, 2))
            path.append((2, 1))
        path.append((1, 3))
        path.append((3, 1))
    return path


T = 6
path = get_path()
utility = get_utility_sequence(graph, path)
draw_utility_sequence(utility, T)
