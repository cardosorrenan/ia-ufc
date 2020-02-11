import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d 


class Noh:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value = np.abs(self.x * np.sin(self.y * np.pi / 4) + self.y * np.sin(self.x * np.pi / 4))


def get_n_searches():
    while True:
        n_searchs = int(input('Number of random searches: '))
        if not n_searchs <= 0:
            break
        print("type a number > 0...")
    print('Local maximums...')
    return n_searchs


def throw_node_field():
    x_init = round(np.random.uniform(-20, 20), 2)
    y_init = round(np.random.uniform(-20, 20), 2)
    return Noh(x_init, y_init)


def calc_neighbors(current_node):
    return [Noh(current_node.x-0.01, current_node.y),
            Noh(current_node.x+0.01, current_node.y),
            Noh(current_node.x, current_node.y+0.01),
            Noh(current_node.x, current_node.y-0.01)]


def find_print_global_max(local_max):
    print('\nGlobal Maximum')
    global_max = max(local_max[it][3] for it in range(0, len(local_max)))
    i_global_max = []
    for local in local_max:
        if round(local[3], 6) == round(global_max, 6):
            print("-- Search nº{}: X:{} Y:{} Z:{}".format(local[0], round(local[1], 2), round(local[2], 2), round(local[3], 6)))
            i_global_max.append(local[0])
    return i_global_max


def func(x, y):
    return np.abs(x * np.sin(y * np.pi / 4) + y * np.sin(x * np.pi / 4))


def plot_result(i_max, path):
    a_x = plt.axes(projection='3d')
    x_plot = np.linspace(-20, 20, 50)
    y_plot = np.linspace(-20, 20, 50)
    x_grid, y_grid = np.meshgrid(x_plot, y_plot)
    z_grid = func(x_grid, y_grid)
    a_x.contour3D(x_grid, y_grid, z_grid, 100, cmap='binary', alpha=0.8)

    for i in i_max:
        for p in path:
            if p[0] == i:
                a_x.scatter(p[1], p[2], p[3], c='red', marker='*', s=10)

    plt.savefig('plot_output/hill_climbing.png')

   
