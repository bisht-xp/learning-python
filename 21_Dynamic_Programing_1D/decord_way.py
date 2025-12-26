# memoization method

# def numDecodings( s: str) -> int:
#     memo = {}
#     def dfs(i):
#         if i >= len(s):
#             return 1
    
#         if s[i] == "0":
#             return 0

#         if i in memo:
#             return memo[i]                

#         left =  dfs(i+1)
#         if i < len(s)-1:
#             if s[i] == "1" or s[i] == "2" and s[i+1] < "7":
#                left += dfs(i+2)
        
#         memo[i] = left

#         return memo[i]
#     return dfs(0)

def numDecodings( s: str) -> int:
    dp = [0]* (len(s) + 1)
    dp[0] = 1

    for i in range(1,len(s)+1):
        if s[i-1] == "0":
            dp[i] = 0
        else:
            left = dp[i-1]
        
        if s[i-1] == "1" or s[i-1] == "2" and s[i-2] < "7":
            left += dp[i-2]
    
        dp[i] = left
    
    return dp[len(s)]

print(numDecodings("1201234"))