import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

       
def hello_darwin():   
    all_individuals = []
    spinner = ['\\','/','-',' ']
    counter_spinner = 0
    index_spinner = 0
    speed_spinner = 10
    for x in range(0, 1024):
        for y in range(0, 1024):
            all_individuals.append(Individual(x, y))
        counter_spinner += 1
        print("Loading all chromosomes... {:.0f}% {}".format((x/1023)*100, spinner[index_spinner%4]), end="\r")
        if counter_spinner == speed_spinner: 
            counter_spinner = 0
            index_spinner += 1
    print("\n")
    return all_individuals


def create_txt_files():
    with open("results/generation.txt", "w+") as myfile:
        myfile.write(" Generation    X           Y             Z              chromosome\n")
    with open("results/mutation.txt", "w+") as myfile:
        myfile.write("")
    with open("results/selection.txt", "w+") as myfile:
        myfile.write("")  
            
            
def plot_result(best_individuals):
    ax = plt.axes(projection='3d')
    x_plot = np.linspace(0, 20, 100)
    y_plot = np.linspace(0, 20, 100)
    x_grid, y_grid = np.meshgrid(x_plot, y_plot)
    z_grid = np.abs(x_grid * np.sin(y_grid * np.pi / 4) + y_grid * np.sin(x_grid * np.pi / 4))
    ax.contour3D(x_grid, y_grid, z_grid, 100, cmap='binary', alpha=0.8)
    for ind in best_individuals:
        ax.scatter(ind.x, ind.y, ind.value, c='red', marker='*', s=100)
    plt.show()