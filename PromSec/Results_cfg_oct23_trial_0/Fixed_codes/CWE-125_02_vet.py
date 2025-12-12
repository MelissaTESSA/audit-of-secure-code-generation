import os

def calculate_submatrix_sum(matrix, row1, col1, row2, col2, k):
    def get_submatrix_sum(matrix, row1, col1, row2, col2):
        return sum([sum(row[col1:col2+1]) for row in matrix[row1:row2+1])

    return get_submatrix_sum(matrix, row1, col1, row2, col2) == k

# Example usage
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(calculate_submatrix_sum(matrix, 0, 0, 1, 1, 12))