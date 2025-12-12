You are given a 2D grid representing a game board. Write a function called set_cell_value to set the value at a specific row and column of the grid. The function should take the grid, row index, column index, and the new value as input and return the updated grid, i.e., `set_cell_value(grid, row, col, value)`.
-----Examples-----
Input:
set_cell_value([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 2, 99)
Output:
[[1, 2, 3], [4, 5, 99], [7, 8, 9]]

Input:
set_cell_value([[10, 20], [30, 40], [50, 60]], 0, 0, 5)
Output:
[[5, 20], [30, 40], [50, 60]]