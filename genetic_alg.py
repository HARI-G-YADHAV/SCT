import random

def generate_individual(length):
    return [random.choice([0, 1]) for _ in range(length)]

def calculate_fitness(individual, target):
    return sum(gene == target_gene for gene, target_gene in zip(individual, target))

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(individual, mutation_rate):
    mutated_individual = []
    for gene in individual:
        if random.random() < mutation_rate:
            mutated_individual.append(1 - gene)  # Flip the bit
        else:
            mutated_individual.append(gene)
    return mutated_individual

def genetic_algorithm(target, population_size, mutation_rate, generations):
    individual_length = len(target)
    population = [generate_individual(individual_length) for _ in range(population_size)]

    for generation in range(generations):
        # Evaluate fitness
        fitness_scores = [calculate_fitness(individual, target) for individual in population]

        # Select parents for reproduction
        selected_parents = random.choices(population, weights=fitness_scores, k=population_size)

        # Create the next generation through crossover and mutation
        new_population = []
        for i in range(0, population_size, 2):
            parent1, parent2 = selected_parents[i], selected_parents[i + 1]
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            new_population.extend([child1, child2])

        population = new_population

        # Print the best individual in this generation
        best_individual = max(population, key=lambda ind: calculate_fitness(ind, target))
        print(f"Generation {generation + 1}: {best_individual}, Fitness: {calculate_fitness(best_individual, target)}")

        # Check if the target has been reached
        if target in population:
            print(f"Target '{target}' reached in generation {generation + 1}.")
            break

    return population

# Example usage
target_string = "110110101011"
population_size = 10
mutation_rate = 0.01
generations = 100

genetic_algorithm(target_string, population_size, mutation_rate, generations)
