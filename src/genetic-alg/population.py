import numpy as np


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
        with open("results/generation.txt", "a") as myfile:
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
    
        with open("results/selection.txt", "a") as myfile:
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