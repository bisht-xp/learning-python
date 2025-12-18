# memoization
# def minDistance(word1: str, word2: str) -> int:
#     memo = {}

#     def dfs(i,j):
#         if i >= len(word1):
#             return len(word2)-j
        
#         if j >= len(word2):
#             return len(word1)-i
        
#         if((i,j) in memo):
#             return memo[(i,j)]
        
#         if word1[i] == word2[j]:
#             return dfs(i+1, j+1)

#         replace = dfs(i+1, j+1) + 1
#         delete = dfs(i+1,j) + 1
#         insert = dfs(i,j+1) + 1

#         memo[(i,j)] =  min(replace, delete, insert)
#         return memo[(i,j)]

#     return dfs(0,0)

def minDistance(word1: str, word2: str) -> int:
    m,n=len(word1),len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    
    for j in range(n+1):
        dp[0][j] = j
    

    for i in range(1, m+1):
        for j in range(1,n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                replace = 1 + dp[i-1][j-1]
                delete = 1 + dp[i-1][j]
                insert = 1 + dp[i][j-1]
                dp[i][j] = min(insert, delete, replace)

    return dp[m][n]

word1 = "horse"
word2 = "ros"

print(minDistance(word1, word2))