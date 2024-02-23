import numpy as np
from genetic_algorithm import genetic_algorithm
from extremities import Extremities
from animation import plot

def eggholder(x, y):
    return -(y + 47) * np.sin(np.sqrt(abs(x/2 + (y + 47)))) - x * np.sin(np.sqrt(abs(x - (y + 47))))

range_x = [-512, 512]
range_y = [-512, 512]

generations, best_individual, best_fitness = genetic_algorithm(eggholder, Extremities.Minima, 1000, range_x, range_y, 0.001, 0.2)

print("Optimal point: ", best_individual)
print("Optimal solution: ", best_fitness)
print("Number of generations: ", len(generations))

plot(eggholder, generations, range_x, range_y)