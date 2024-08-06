import numpy as np
# Number of faces on each die
num_faces = 6

# Total combinations
total_combinations = num_faces * num_faces
print("Total combinations:", total_combinations)

# Number of faces on each die
num_faces = 6

# Initialize a 6x6 matrix to hold the distribution
distribution_matrix = np.zeros((num_faces, num_faces), dtype=int)

# Fill the matrix with counts of sums
for die_a in range(1, num_faces + 1):
    for die_b in range(1, num_faces + 1):
        sum_ab = die_a + die_b
        distribution_matrix[die_a - 1][die_b - 1] = sum_ab

print("Distribution matrix of sums:")
print(distribution_matrix)

# Initialize a dictionary to hold the counts of each sum
sum_counts = {i: 0 for i in range(2, 13)}

# Calculate the counts for each sum
for die_a in range(1, num_faces + 1):
    for die_b in range(1, num_faces + 1):
        sum_ab = die_a + die_b
        sum_counts[sum_ab] += 1

# Calculate probabilities
total_combinations = num_faces * num_faces
probabilities = {sum_val: count / total_combinations for sum_val, count in sum_counts.items()}

print("Sum counts:", sum_counts)
print("Probabilities of each sum:")
for sum_val, prob in probabilities.items():
    print(f"P(Sum = {sum_val}) = {prob:.4f}")