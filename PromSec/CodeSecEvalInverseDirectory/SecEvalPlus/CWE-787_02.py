Given a list of lists, where each inner list represents a row of a matrix, write a function called set_matrix_value to set the value at a specific row and column of the matrix. The function should take the matrix, row index, column index, and the new value as input and return the updated matrix.
-----Examples-----
Input:
set_matrix_value([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 2, 99)
Output:
[[1, 2, 3], [4, 5, 99], [7, 8, 9]]

Input:
set_matrix_value([[10, 20], [30, 40], [50, 60]], 0, 0, 5)
Output:
[[5, 20], [30, 40], [50, 60]]

Input:
set_matrix_value([[100]], 0, 0, 200)
Output:
[[200]]
