import random

def fitness(x):
    return sum(x)

def genetic_algorithm():
    population = [[random.randint(10,50) for _ in range(4)] for _ in range(10)]

    for _ in range(50):
        population = sorted(population, key=fitness)
        population = population[:5]

        new_pop = population.copy()
        while len(new_pop) < 10:
            p1, p2 = random.sample(population, 2)
            child = p1[:2] + p2[2:]
            new_pop.append(child)

        population = new_pop

    return min(population, key=fitness)

print(genetic_algorithm())
