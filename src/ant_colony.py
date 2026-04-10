import numpy as np
import random

# number of signals (e.g., 4 directions)
NUM_SIGNALS = 4
NUM_ANTS = 10
ITERATIONS = 50

# pheromone matrix
pheromone = np.ones((NUM_SIGNALS, 50))

def fitness(solution):
    # minimize waiting time (simple simulation)
    return sum(solution)

def generate_solution():
    return [random.randint(10, 60) for _ in range(NUM_SIGNALS)]

def update_pheromone(solutions):
    global pheromone
    pheromone *= 0.9  # evaporation

    for sol in solutions:
        score = fitness(sol)
        for i in range(NUM_SIGNALS):
            pheromone[i][sol[i]-10] += 1.0 / (score + 1)

def ant_colony():
    best_solution = None
    best_score = float('inf')

    for _ in range(ITERATIONS):
        solutions = []

        for _ in range(NUM_ANTS):
            sol = generate_solution()
            solutions.append(sol)

            score = fitness(sol)
            if score < best_score:
                best_score = score
                best_solution = sol

        update_pheromone(solutions)

    return best_solution, best_score

if __name__ == "__main__":
    solution, score = ant_colony()
    print("Best Signal Timing:", solution)
    print("Minimum Waiting Time:", score)
