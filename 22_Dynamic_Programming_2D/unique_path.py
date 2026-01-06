# Top down approch

# def uniquePaths(m: int, n: int) -> int:

#     cache = {}
#     def dfs(i,j):
#         if i >= m or j>=n:
#             return 0

#         if i == m-1 and j == n-1:
#             return 1
        
#         if (i,j) in cache:
#             return cache[(i,j)]
        
#         cache[(i,j)] =  (dfs(i+1,j) + dfs(i,j+1))
#         return cache[(i,j)]
    
#     return dfs(0,0)

def uniquePaths(m: int, n: int) -> int:
    dp = [[0]*n for _ in range(m)]

    for i in range(m):
        dp[i][0] = 1
    
    for j in range(n):
        dp[0][j] = 1

    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

print(uniquePaths(4,4))