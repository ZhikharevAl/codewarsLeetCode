import numpy as np

def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b):
        return []
    result = np.dot(matrix_a, matrix_b)
    return result.tolist()
