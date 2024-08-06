from collections import defaultdict

def calculate_combinations(die_a, die_b):
    count = 0
    for i in die_a:
        for j in die_b:
            count += 1
    return count

def generate_all_combinations(die_a, die_b):
    combinations = []
    for i in die_a:
        for j in die_b:
            combinations.append([i, j])
    return combinations

def calculate_probabilities(die_a, die_b):
    combinations = []
    for i in die_a:
        for j in die_b:
            combinations.append(i + j)
    count = defaultdict(int)
    probabilities = {}
    total_combinations = len(combinations)
    for i in combinations:
        count[i] += 1
    for i in range(2, 13):
        count_i = count.get(i, 0)
        probability_i = count_i / total_combinations
        probabilities[i] = {"count": count_i, "probability": round(probability_i, 5)}
    return probabilities

def undoom_dice(die_a, die_b):
    new_die_a = [min(i, 4) for i in die_a]
    new_die_b = die_b  # This function does not modify Die_B, as there is no constraint on Die_B
    return sorted(new_die_a), sorted(new_die_b)

def main():
    die_a = range(1, 7)
    die_b = range(1, 7)
    
    # Calculate original probabilities
    original_probabilities = calculate_probabilities(die_a, die_b)
    
    # Generate all possible combinations of the original dice
    all_combinations = generate_all_combinations(die_a, die_b)
    
    # Transform dice according to the constraints
    new_die_a, new_die_b = undoom_dice(list(die_a), list(die_b))
    
    # Calculate modified probabilities
    modified_probabilities = calculate_probabilities(new_die_a, new_die_b)
    
    # Print results
    print("Total Combinations:", calculate_combinations(die_a, die_b))
    print("All Combinations:")
    for combination in all_combinations:
        print(combination)
    
    print("\nOriginal Probabilities:")
    for sum_combination, probability in original_probabilities.items():
        print(f"Sum: {sum_combination}, Count: {probability['count']}, Probability: {probability['probability']}")
    
    print("\nModified Probabilities:")
    for sum_combination, probability in modified_probabilities.items():
        print(f"Sum: {sum_combination}, Count: {probability['count']}, Probability: {probability['probability']}")

if __name__ == "__main__":
    main()
