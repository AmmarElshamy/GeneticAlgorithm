from extremities import Extremities

def fitness(population, fitness_function, extremity: Extremities):
    """    
    Calculate the fitness of the population.
    
    Parameters
    ----------
    population: list
        The population to calculate the fitness
    fitness_function: function
        The fitness function
    extremity: Extremities
        The extremity of the fitness function
    
    Returns
    -------
    list
        The population with its calculated fitness score
    """
    if extremity == Extremities.Minima:
        population_fitness = [[[p[0], p[1]], -fitness_function(p[0], p[1])] for p in population]
    else:
        population_fitness = [[[p[0], p[1]], fitness_function(p[0], p[1])] for p in population]
        
    return population_fitness