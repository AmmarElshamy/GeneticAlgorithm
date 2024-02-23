import numpy as np
from initial_population import random_init_population
from termination import check_termination
from fitness import fitness
from selection import rank_selection, roulette_wheel_selection
from crossover import crossover
from mutation import mutation
from extremities import Extremities

def genetic_algorithm(fitness_function, extremity: Extremities, population_size, x_bounds, y_bounds, termination_threshold, mutation_rate):
    """
    genetic_algorithm(fitness_function, extremity, population_size, x_bounds, y_bounds, termination_threshold, mutation_rate) -> list, list, float
    Run a genetic algorithm to optimize a 2D function.
    
    Parameters
    ----------
    fitness_function: function
        The fitness function to optimize.
    extremity: Extremities
        The extremity of the optimization problem.
    population_size: int
        The number of individuals in the population.
    x_bounds: list
        The range of values for the x-axis.
    y_bounds: list
        The range of values for the y-axis.
    termination_threshold: float
        The threshold for the standard deviation of the fitness values.
    mutation_rate: float
        The mutation rate.
        
    Returns
    -------
    list
        The generations of the genetic algorithm.
    list
        The best individual in the last generation.
    float
        The fitness of the best individual.
    """
    generation_number = 0
    generation_max_count = 0
    
    initial_population = random_init_population(population_size, x_bounds, y_bounds)
    population_fitness = fitness(initial_population, fitness_function, extremity)
    max_fitness = max([x[1] for x in population_fitness])
    generations = [initial_population]
    
    while not check_termination(population_fitness, termination_threshold, generation_max_count):
        if max([x[1] for x in population_fitness]) > max_fitness:
            max_fitness = max([x[1] for x in population_fitness])
            generation_max_count = 0
        else:
            generation_max_count += 1
            
        pool = rank_selection(population_fitness)
        offspring = crossover(pool)
        population = mutation(offspring, mutation_rate, generation_number)
        generations.append(population)
        population_fitness = fitness(population, fitness_function, extremity)
        generation_number += 1
        
    best_population = generations[-1]
    best_individual, best_fitness = max([(individual, fitness_function(*individual)) for individual in population], key=lambda x: x[1])
    
    return generations, best_individual, best_fitness