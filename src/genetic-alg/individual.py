import numpy as np


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
        with open("results/mutation.txt", "a") as myfile:
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