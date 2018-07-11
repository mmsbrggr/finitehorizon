import numpy as np
from graph import get_utility_sequence
from config import INFINITY
from visuals import draw_utility_sequence

number_nodes = 5
graph = [[(-np.inf, -np.inf) for x in range(number_nodes)] for y in range(number_nodes)]

graph[0][1] = (3, 0)
graph[1][2] = (-1, 1)
graph[2][1] = (0, 0)
graph[1][4] = (4, -4)
graph[4][1] = (0, 0)
graph[2][3] = (0, 1)
graph[3][1] = (0, 0)


def get_path_1():
    path = []
    path.append((0, 1))
    path.append((1, 2))
    path.append((2, 3))
    path.append((3, 1))
    for i in range(INFINITY // 4):
        j = 2 if i is 0 else 4
        for _ in range(j):
            path.append((1, 2))
            path.append((2, 1))
        path.append((1, 4))
        path.append((4, 1))
    return path


def get_path_2():
    path = []
    path.append((0, 1))
    for _ in range(INFINITY // 4):
        for _ in range(2):
            path.append((1, 2))
            path.append((2, 3))
            path.append((3, 1))
        path.append((1, 4))
        path.append((4, 1))
    return path


T = 6
path = get_path_2()
utility = get_utility_sequence(graph, path)
draw_utility_sequence(utility, T)
