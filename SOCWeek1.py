
import numpy as np

# Define the row vector and the 4x4 matrix
row_vector = np.array([0, 1, 0, 0])
matrix = np.array([
   [1, 0, 0, 0],
    [0.5, 0, 0.5, 0],
    [0, 0.2, 0, 0.8],
    [0, 0, 0, 1]
])


# Iterate 100 times
for _ in range(100):
    row_vector = np.dot(row_vector, matrix)

print("Resultant row vector after 100 iterations:")
print(row_vector)