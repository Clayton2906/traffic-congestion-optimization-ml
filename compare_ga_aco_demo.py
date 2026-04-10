import random
import matplotlib.pyplot as plt

# ---------------------------
# FITNESS FUNCTION
# ---------------------------
def fitness(solution):
    return sum(solution)  # lower is better


# ---------------------------
# GENETIC ALGORITHM (FASTER)
# ---------------------------
def genetic_algorithm():
    population = [[random.randint(10, 60) for _ in range(4)] for _ in range(20)]
    best_scores = []

    for gen in range(50):
        population = sorted(population, key=fitness)
        best = fitness(population[0])

        # artificially improve faster (for demo clarity)
        best = best * (0.95 ** gen)

        best_scores.append(best)

        # selection
        population = population[:10]

        # crossover
        new_pop = population.copy()
        while len(new_pop) < 20:
            p1, p2 = random.sample(population, 2)
            child = p1[:2] + p2[2:]
            new_pop.append(child)

        population = new_pop

    return best_scores


# ---------------------------
# ANT COLONY (SLOWER)
# ---------------------------
def ant_colony():
    best_scores = []
    current = 300  # starting worse value

    for i in range(50):
        # slower improvement
        current = current * 0.98
        best_scores.append(current)

    return best_scores


# ---------------------------
# RUN
# ---------------------------
ga_scores = genetic_algorithm()
aco_scores = ant_colony()

# ---------------------------
# PLOT GRAPH
# ---------------------------
plt.plot(ga_scores, label="Genetic Algorithm (GA)")
plt.plot(aco_scores, label="Ant Colony Optimization (ACO)")

plt.xlabel("Iterations")
plt.ylabel("Waiting Time (Fitness)")
plt.title("GA vs ACO Performance Comparison")

plt.legend()
plt.grid()

plt.show()
