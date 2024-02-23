import random

def random_init_population(population_size, range_x, range_y):
    """
    random_init_population(population_size, range_x, range_y) -> list
    
    Generate a random initial population for a 2D optimization problem.
    
    Parameters
    ----------
    population_size: int
        The number of individuals in the population
    range_x: list
        The range of values for the x-axis
    range_y: list
        The range of values for the y-axis
    
    Returns
    -------
    list
        A random initial population
    """
    return [[random.uniform(range_x[0], range_x[1]), random.uniform(range_y[0], range_y[1])] for _ in range(population_size)]