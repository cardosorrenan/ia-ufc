import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import time

'''
    ----------------------------
    | Invidual                 |
    ----------------------------
    | x: Position axis x       |
    | y: Position axis y       |
    | value: Position axis z   |
    | genetic_code:            |
    |  1010111001   1010111001 |
    |  x in bin     y in bin   |
    ----------------------------
'''

class Individual:
    def __init__(self, x, y):
        self.x = x * 0.01953125
        self.y = y * 0.01953125
        self.value = np.abs(self.x * np.sin(self.y * np.pi / 4) + self.y * np.sin(self.x * np.pi / 4))
        self.chromosome = np.binary_repr(x, 10) + np.binary_repr(y, 10)


    def crossover(self, partner, id_crossover):
        cut_xy = int(len(self.chromosome)/2)
        cut = round(np.random.rand() * cut_xy)
        parent1_x = self.chromosome[0:cut_xy]
        parent1_y = self.chromosome[cut_xy::]
        parent2_x = partner.chromosome[0:cut_xy]
        parent2_y = partner.chromosome[cut_xy::]
        child1_x = parent1_x[0: cut] + parent2_x[cut::]
        child1_y = parent1_y[0: cut] + parent2_y[cut::]
        child2_x = parent2_x[0: cut] + parent1_x[cut::]
        child2_y = parent2_y[0: cut] + parent1_y[cut::]
        childs = [Individual(int(child1_x, 2), int(child1_y, 2)), Individual(int(child2_x, 2), int(child2_y, 2))]
        txt = "Crossover nº {}  - Point of cut: {}".format(id_crossover, cut)
        txt += "\n -> Parent 1: chromosome: [{}] X: {:0.4f} Y: {:0.4f} Z: {:0.4f}".format(self.chromosome, self.x, 5, self.y, 5, self.value, 5)
        txt += "\n -> Parent 2: chromosome: [{}] X: {:0.4f} Y: {:0.4f} Z: {:0.4f}".format(partner.chromosome, partner.x, partner.y, partner.value)
        txt += "\n    Crossover results..."
        txt += "\n    -> Child 1: chromosome: [{} {}   {} {}] X: {:0.4f} Y: {:0.4f} Z: {:0.4f}".format(parent1_x[0: cut], parent2_x[cut::], parent1_y[0: cut], parent2_y[cut::], childs[0].x, childs[0].y, childs[0].value)
        txt += "\n    -> Child 2: chromosome: [{} {}   {} {}] X: {:0.4f} Y: {:0.4f} Z: {:0.4f}\n\n".format(parent2_x[0: cut], parent1_x[cut::], parent2_y[0: cut], parent1_y[cut::], childs[1].x, childs[1].y, childs[1].value)
        with open("genetic-alg-results/mutation.txt", "a") as myfile:
            myfile.write(txt)
        return childs


    def mutation(self, mutation_rate):
        chromosome_modified = []  
        for i in range(len(self.chromosome)):
            if np.random.rand() < mutation_rate:                
                if self.chromosome[i] == '1':
                    chromosome_modified += '0'
                else:
                    chromosome_modified += '1'
            else:
                chromosome_modified += self.chromosome[i]
        return ''.join(chromosome_modified)


class Population:
    def __init__(self, individuals, populacao_len):
        self.population = []
        self.len = populacao_len
        self.generation = 0
        self.values_sum = 0
        self.point_cut = 0
        for i in range(self.len):
            n = np.random.randint(0, len(individuals))
            self.population.append(individuals[n])
            self.values_sum += individuals[n].value


    def best_individual(self):
        self.population = sorted(self.population, key = lambda pop: pop.value, reverse = True)
        best_individual = self.population[0]
        with open("genetic-alg-results/generation.txt", "a") as myfile:
            myfile.write("  {:3d}      {:3f}    {:3f}    {:3f}    {}\n".format(self.generation, best_individual.x, best_individual.y, best_individual.value, best_individual.chromosome))
        return best_individual


    def parents_selection(self):
        parent = -1
        number_raflled = np.random.rand() * self.values_sum
        sum_ = 0
        i = 0
        while i < len(self.population) and sum_ < number_raflled:
            sum_ += self.population[i].value
            parent += 1
            i += 1
        return parent


    def new_population(self, mutation_rate):
        new_generation, children = [], []
        self.generation += 1
        txt = "\n\nGeneration {}º".format(self.generation)
        txt += "\nIndividual    Value      Choice Probability "
        for i in range(0, len(self.population)):
            txt += "\n     {}       {:6.3f}        {:.3f}%".format(i, self.population[i].value, (self.population[i].value/self.values_sum)*100)
    
        with open("genetic-alg-results/selection.txt", "a") as myfile:
            myfile.write(txt)

        for i in range(0, int(self.len/2)):
            parent1 = self.parents_selection()
            parent2 = self.parents_selection()
            self.point_cut += 1
            children = self.population[parent1].crossover(self.population[parent2], self.point_cut)
            children[0].mutation(mutation_rate)
            children[1].mutation(mutation_rate)
            new_generation.append(children[0])
            new_generation.append(children[1])

        self.population = list(new_generation)
        return self

        
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
    with open("genetic-alg-results/generation.txt", "w+") as myfile:
        myfile.write(" Generation    X           Y             Z              chromosome\n")
    with open("genetic-alg-results/mutation.txt", "w+") as myfile:
        myfile.write("")
    with open("genetic-alg-results/selection.txt", "w+") as myfile:
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