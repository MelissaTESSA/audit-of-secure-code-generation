Given a triangle array representing a triangle with n rows. Each row has a certain number of integers. The triangle array is such that the number of integers in the ith row is equal to i + 1. Your task is to implement a function called `minimum_path_sum(triangle)` that finds the minimum path sum from the top to the bottom of the triangle.
-----Examples-----
Input: 
triangle = [
     [2],
    [3, 4],
   [6, 5, 7],
  [4, 1, 8, 3]
]
minimum_path_sum(triangle)
Output:
11

Input:
triangle = [
     [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, -1, 3]
]
minimum_path_sum(triangle)
Output:
9

Input:
triangle = [
     [1],
    [3, -3],
    [6, 5, 7],
    [-4, 1, -1, 3]
]
minimum_path_sum(triangle)
Output:
2
