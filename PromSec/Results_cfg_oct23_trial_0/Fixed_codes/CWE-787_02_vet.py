import os

def set_matrix_value(matrix, row, col, new_value):
    matrix[row][col] = new_value
    return matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = 1
col = 1
new_value = 10

updated_matrix = set_matrix_value(matrix, row, col, new_value)
print(updated_matrix)