from functions_genetic_alg import *
from individual import Individual
from population import Population


create_txt_files()

population_len = 50 # Number of individuals in populations
mutation_rate = 0.05 # Chance of occur a mutation on chromosome
generations_len = 20

individuals = hello_darwin() # Returns 1048576 (1024x1024) individuals, or chromosomes :D
population = Population(individuals, population_len) # Create a new population

selected = []
for gen in range(generations_len):
    best_in_population = population.best_individual()
    selected.append(best_in_population)
    population = population.new_population(mutation_rate)

thomas_anderson = sorted(selected, key=lambda pop: pop.value, reverse=True)[0]
print("The One:\n       x = {}\n       y = {:3f}\n  f(x,y) = {:3f}\n".format(thomas_anderson.x, thomas_anderson.y, thomas_anderson.value))
plot_result(selected)
                                                                  