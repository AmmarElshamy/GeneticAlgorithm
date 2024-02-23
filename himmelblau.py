from genetic_algorithm import genetic_algorithm
from extremities import Extremities
from animation import plot

def himmelblau(x, y):
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

range_x = [-5, 5]
range_y = [-5, 5]

generations, best_individual, best_fitness = genetic_algorithm(himmelblau, Extremities.Minima, 1000, range_x, range_y, 0.0001, 0.2)

print("Optimal point: ", best_individual)
print("Optimal solution: ", best_fitness)
print("Number of generations: ", len(generations))

plot(himmelblau, generations, range_x, range_y)