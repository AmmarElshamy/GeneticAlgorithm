from genetic_algorithm import genetic_algorithm
from extremities import Extremities
from animation import plot

def rosenbrock(x, y):
    return 100 * (y - x**2)**2 + (1 - x)**2

range_x = [-4, 4]
range_y = [-4, 4]

generations, best_individual, best_fitness = genetic_algorithm(rosenbrock, Extremities.Minima, 1000, range_x, range_y, 0.0001, 0.2)

print("Optimal point: ", best_individual)
print("Optimal solution: ", best_fitness)
print("Number of generations: ", len(generations))

plot(rosenbrock, generations, range_x, range_y)