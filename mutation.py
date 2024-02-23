import numpy as np

def mutation(offspring, mutation_rate, generation_number):
    """
    Mutate the offspring using the mutation method.
    
    Parameters
    ----------
    offspring: list
        The offspring to be mutated.
    mutation_rate: float
        The mutation rate.
    generation_number: int
        The number of the generation.
        
    Returns
    -------
    list
        The mutated offspring.
    """
    additional_value = np.random.normal(0.0, 1/(generation_number + 1))
    # additional_value = max(0, additional_value)
    
    population_size = len(offspring)
    genes_count = 2
    number_of_mutations = int(population_size * genes_count * mutation_rate)
    
    mutated = set()
    mutation_count = 0
    while mutation_count < number_of_mutations:
        c = np.random.randint(0, population_size - 1)
        g = np.random.randint(0, genes_count - 1)
        if (c, g) not in mutated:
            offspring[c][g] += np.random.randn() * additional_value
            mutated.add((c, g))
            mutation_count += 1
            
    return offspring