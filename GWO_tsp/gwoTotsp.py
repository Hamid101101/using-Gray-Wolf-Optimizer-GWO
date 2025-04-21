import numpy as np

def generate_random_tours(population_size, num_cities):
    initial_population = [np.random.permutation(range(num_cities)) for _ in range(population_size)]
    return initial_population

def calculate_total_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour)):
        total_distance += distance_matrix[tour[i - 1]][tour[i]]
    return total_distance

def is_full_tour(tour, num_cities):
    return len(set(tour)) == num_cities

def grey_wolf_optimization_tsp(num_cities, population_size, max_iterations, distance_matrix):
    population = generate_random_tours(population_size, num_cities)

    for iteration in range(max_iterations):
        fitness_values = [calculate_total_distance(tour, distance_matrix) for tour in population]

        max_fitness_index = np.argmax(fitness_values)
        population.pop(max_fitness_index)

        if is_full_tour(population[0], num_cities):
            break

        for i in range(population_size):
            alpha = min(population, key=lambda x: calculate_total_distance(x, distance_matrix))
            beta = min([x for x in population if not np.array_equal(x, alpha)], key=lambda x: calculate_total_distance(x, distance_matrix))
            delta = min([x for x in population if not np.array_equal(x, alpha) and not np.array_equal(x, beta)], key=lambda x: calculate_total_distance(x, distance_matrix))

            population[i] = (population[i] + alpha) % num_cities
            population[(i + 1) % population_size] = (population[(i + 1) % population_size] + beta) % num_cities
            population[(i + 2) % population_size] = (population[(i + 2) % population_size] + delta) % num_cities

    best_solution = min(population, key=lambda x: calculate_total_distance(x, distance_matrix))
    return best_solution

moroccan_cities = ["Casablanca", "Marrakech", "Rabat", "Fes", "Tangier"]
num_cities = len(moroccan_cities)
population_size = 500
max_iterations = 10000

distance_matrix = np.array([[0, 200, 90, 300, 400],
                            [200, 0, 250, 150, 350],
                            [90, 250, 0, 180, 280],
                            [300, 150, 180, 0, 200],
                            [400, 350, 280, 200, 0]])

best_solution = grey_wolf_optimization_tsp(num_cities, population_size, max_iterations, distance_matrix)

print("Best route:", [moroccan_cities[i] for i in best_solution])
print("Total distance traveled:", calculate_total_distance(best_solution, distance_matrix))
