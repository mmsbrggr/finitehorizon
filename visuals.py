import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from config import INFINITY
from adversary import get_optimal_path_info


def draw_utility_sequence(u, T):
    plt.axhline(0, color='gray')
    plt.axvline(T, color='gray')

    points = np.asarray([[i, u[i]] for i in range(INFINITY)])
    plt.plot(points[:, 0], points[:, 1], "-o")

    path_info = get_optimal_path_info(u, T)
    newline((path_info['t1'], u[path_info['t1']]), (path_info['t2'], u[path_info['t2']]), color="red")

    plt.xlim(0, 30)
    plt.ylim(-4, 70)
    plt.show()


def newline(p1, p2, color=None):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax], color=color)
    ax.add_line(l)
    return l
