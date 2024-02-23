import numpy as np

def check_termination(population_fitness, threshold, max_fitness_count):
    """
    Check the termination criteria for the genetic algorithm.
    
    Parameters
    ----------
    population_fitness: list
        The fitness of the population.
    threshold: float
        The threshold for the standard deviation of the fitness values.
    max_fitness_count: int
        The number of generations the maximal fitness does not change.
        
    Returns
    -------
    bool
        True if the termination criteria are met, False otherwise.
    """
    return np.std([x[1] for x in population_fitness]) < threshold and max_fitness_count >= 5