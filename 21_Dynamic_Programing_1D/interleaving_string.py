
# Memoization

# def isInterleave(s1: str, s2: str, s3: str) -> bool:
#     if(len(s1) + len(s2) != len(s3)):
#         return False
#     memo = {}
#     def dfs(i,j):
#         if i >= len(s1) and j >= len(s2):
#             return True
        
#         if (i,j) in memo:
#             return memo[(i,j)]

#         k = i+j
#         take_s1 = False
#         if i < len(s1) and  s1[i] == s3[k]:
#             take_s1 = dfs(i+1,j)
        
#         take_s2 = False
#         if j < len(s2) and s2[j] == s3[k]:
#             take_s2 = dfs(i,j+1)
        
#         memo[(i,j)] = take_s1 or take_s2

#         return memo[(i,j)]

#     return dfs(0,0)


# Tabulation 

def isInterleave(s1: str, s2: str, s3: str) -> bool:
    
    m = len(s1)
    n=len(s2)

    if m+n != len(s3):
        return False
    
    dp = [[False]*(n+1) for _ in range(m+1)]

    dp[0][0] = True

    for i in range(1, m+1):
        dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
    
    for i in range(1, n+1):
        dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]

    for i in range(1, m+1):
        for j in range(1, n+1):
            curr = s3[i+j-1]
            take1 = dp[i-1][j] and s1[i-1] == curr
            take2 = dp[i][j-1] and s2[j-1] == curr

            dp[i][j] = take1 or take2
    

    return dp[m][n]




s1 = "aabd"
s2 = "abdc" 
s3 = "aabdabcd"

print(isInterleave(s1,s2,s3))


