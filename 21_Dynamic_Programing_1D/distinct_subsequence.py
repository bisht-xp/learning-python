# memorization method
# def numDistinct( s: str, t: str) -> int:
#     memo = {}
#     def dfs(i,j):
#         if(j == len(t)):
#             return 1
        
#         if i >= len(s):
#             return 0

#         if (i,j) in memo:
#             return memo[(i,j)]

#         if(s[i] == t[j]):
#             memo[(i,j)] = dfs(i+1,j+1) + dfs(i+1, j)
#         else:
#             memo[(i,j)] = dfs(i+1, j)
        
#         return memo[(i,j)]
        
#     return dfs(0,0)

def numDistinct( s: str, t: str) -> int:
    dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

    for i in range(len(s)+1):
        dp[i][0] = 1
    
    for i in range(1,len(s)+1):
        for j in range(1, len(t)+1):
            if(s[i-1] == t[j-1]):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[len(s)][len(t)]


print(numDistinct("babgbag", "bag"))
