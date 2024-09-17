import numpy as np

def minor(matrix, i, j):
    sub_matrix = np.delete(np.delete(matrix, i, axis=0), j, axis=1)
    return np.linalg.det(sub_matrix)

def cofactor_matrix(matrix):
    cofactors = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            cofactors[i][j] = ((-1) ** (i + j)) * minor(matrix, i, j)
    return cofactors

def transpose(matrix):
    return matrix.T

def get_matrix_input():
    matrix = []
    print("Enter the elements of a 3x3 matrix")
    for i in range(3):
        row = list(map(float, input(f"Enter row {i+1} elements (separate by spaces): ").split()))
        if len(row) != 3:
            print("Please enter exactly 3 elements for each row.")
            return None
        matrix.append(row)
    return np.array(matrix)

matrix = get_matrix_input()

if matrix is not None:
    cofactor_mat = cofactor_matrix(matrix)
    transpose_cofactor = transpose(cofactor_mat)
    print("\nOriginal Matrix:")
    print(matrix)
    print("\nCofactor Matrix:")
    print(cofactor_mat)
    print("\nTranspose Matrix:")
    print(transpose_cofactor)
else:
    print("Matrix input was invalid.")
