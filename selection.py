import random
import numpy as np

def roulette_wheel_selection(population_fitness):
    """
    Select individuals from the population using the roulette wheel selection method.
    
    Parameters
    ----------
    population_fitness: list
        The fitness of the population.
        
    Returns
    -------
    list
        The selected individuals from the population.
    """
    population = [pf[0] for pf in population_fitness]
    fitness = [pf[1] for pf in population_fitness]
    weights = [f / sum(fitness) for f in fitness]
    
    pool = random.choices(population, weights=weights, k=len(population_fitness))
    
    return pool


def rank_selection(population_fitness):
    """
    Select individuals from the population using the rank selection method.
    
    Parameters
    ----------
    population_fitness: list
        The fitness of the population.
        
    Returns
    -------
    list
        The selected individuals from the population.
    """
    n = len(population_fitness)
    population = [pf[0] for pf in sorted(population_fitness, key=lambda x: x[1])]
    weights = [(rank + 1) / (n * (n + 1)) for rank in range(n)]
    
    pool = random.choices(population, weights=weights, k=n)
    
    return pool