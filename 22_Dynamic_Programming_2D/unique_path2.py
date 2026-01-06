# Top down approch
# def uniquePathsWithObstacles( obstacleGrid: list[list[int]]) -> int:
#     rows,cols = len(obstacleGrid),len(obstacleGrid[0])
#     cache = {}
#     def dfs(i,j):
#         if i >= rows or j>=cols or obstacleGrid[i][j] == 1:
#             return 0
        
#         if i == rows-1 and j == cols-1:
#             return 1
        
#         if (i,j) in cache:
#             return cache[(i,j)]

#         cache[(i,j)] = dfs(i+1,j) + dfs(i,j+1)
#         return cache[(i,j)]
#     result = dfs(0,0)
#     return result

# bottom-up approch:

def uniquePathsWithObstacles( obstacleGrid: list[list[int]]) -> int:
    rows,cols = len(obstacleGrid),len(obstacleGrid[0])
    dp = [[0]*cols for _ in range(rows)]

    for i in range(rows):
        if obstacleGrid[i][0] == 1:
            break
        dp[i][0] = 1
    
    for j in range(cols):
        if obstacleGrid[0][j] == 1:
            break
        dp[0][j] = 1

    for i in range(1,rows):
        for j in range(1,cols):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[rows-1][cols-1]

obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(obstacleGrid))
        