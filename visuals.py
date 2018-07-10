from tkinter import *
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.lines as mlines
from config import INFINITY
from adversary import get_optimal_path_info

master = None
canvas = None
figure = None


def draw_utility_sequence(u, T):
    global master
    master = Tk()
    master.title("Utility sequence")

    scale = Scale(master, from_=0, to=30, orient=HORIZONTAL, command=lambda v: draw_figure(u, int(v)))
    scale.set(T)
    scale.pack(side=TOP, fill=BOTH, expand=True)

    mainloop()


def draw_figure(u, T, maxT=30):
    global master, canvas, figure
    if figure is None:
        figure = Figure(figsize=(5, 10), dpi=100)
    else:
        figure.clf()

    draw_component(211, [e[0] for e in u], T, maxT)
    draw_component(212, [e[1] for e in u], T, maxT)

    if canvas is None:
        canvas = FigureCanvasTkAgg(figure, master)
        toolbar = NavigationToolbar2TkAgg(canvas, master)
        tk_canvas = canvas.get_tk_widget()
        tk_canvas.pack(side=TOP, fill=BOTH, expand=True)

    canvas.draw()


def draw_component(component, u, T, maxT=30):
    global figure
    p = figure.add_subplot(component)

    p.axhline(0, color='black', linewidth=1)
    p.axvline(T, color='gray', linewidth=1)
    p.set_xlim(0, maxT)
    p.set_ylim(-4, 10)

    points = np.asarray([[i, u[i]] for i in range(INFINITY)])
    p.plot(points[:, 0], points[:, 1], ".-", color='black')

    path_info = get_optimal_path_info(u, T)
    newline(figure, (path_info['t1'], u[path_info['t1']]), (path_info['t2'], u[path_info['t2']]), color="red")


def newline(figure, p1, p2, color=None):
    ax = figure.gca()
    xmin, xmax = ax.get_xbound()

    if p2[0] == p1[0]:
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax], color=color, linewidth=1)
    ax.add_line(l)
    return l
