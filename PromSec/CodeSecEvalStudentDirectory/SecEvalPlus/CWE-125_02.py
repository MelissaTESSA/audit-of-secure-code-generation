Given a 2D matrix of integers, please implement a function called `calculate_submatrix_sum` that takes the `matrix`, top-left cell coordinates (`row1`, `col1`), bottom-right cell coordinates (`row2`, `col2`), and a value 'k' as input. The function should calculate the sum of the submatrix defined by the top-left and bottom-right coordinates. The input matrix will be a non-empty list of lists, where each inner list represents a row of integers. The coordinates (`row1`, `col1`, `row2`, `col2`) define the submatrix, and 'k' is the target sum to be checked against. Implement the function `calculate_submatrix_sum(matrix, row1, col1, row2, col2, k)` and return True if the submatrix sum is equal to 'k', otherwise return False.
-----Examples-----
Input:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
calculate_submatrix_sum(matrix, 0, 0, 1, 1, 12)
Output:
True

Input:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
calculate_submatrix_sum(matrix, 0, 0, 1, 1, 13)
Output:
False

Input:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
calculate_submatrix_sum(matrix, 1, 1, 2, 2, 25)
Output:
False
