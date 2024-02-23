import random

def crossover(pool):
    """
    Create offspring from the mating pool using the crossover method.
    
    Parameters
    ----------
    pool: list
        The mating pool.
        
    Returns
    -------
    list
        The offspring created from the mating pool.
    """
    random.shuffle(pool)
    
    offspring = []
    for i in range(0, len(pool), 2):
        crossover_point = random.randint(0, 2)
        parent1, parent2 = pool[i], pool[i+1]
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        offspring.append(child1)
        offspring.append(child2)
        
    return offspring