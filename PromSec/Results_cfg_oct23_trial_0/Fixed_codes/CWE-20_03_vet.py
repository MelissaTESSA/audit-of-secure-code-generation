import sys

def minimum_path_sum(triangle):
    n = len(triangle)
    dp = triangle[-1]
    
    for i in range(n-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
    
    return dp[0]

triangle = [
     [2],
    [3, 4],
   [6, 5, 7],
  [4, 1, 8, 3]
]
print(minimum_path_sum(triangle))

triangle = [
     [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, -1, 3]
]
print(minimum_path_sum(triangle))

triangle = [
     [1],
    [3, -3],
    [6, 5, 7],
    [-4, 1, -1, 3]
]
print(minimum_path_sum(triangle))