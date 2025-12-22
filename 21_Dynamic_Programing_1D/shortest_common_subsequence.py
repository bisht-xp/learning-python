
# memoization method (TLE cause string is immutable create new space in memory)
# def shortestCommonSupersequence(str1: str, str2: str) -> str:
#     memo = {}    
#     def dfs(i,j):
#         if (i,j) in memo:
#             return memo[(i,j)]
        
#         if(i >= len(str1) or j >= len(str2)):
#             return str2[j:] if i >= len(str1) else str1[i:]


#         if str1[i] == str2[j]:
#             memo[(i,j)] = str1[i] + dfs(i+1,j+1)
#         else:
#             take1 = str1[i] + dfs(i+1,j)
#             take2 = str2[j] + dfs(i,j+1)

#             memo[(i,j)] = take1 if len(take1) < len(take2) else take2

#         return memo[(i,j)]
#     return dfs(0,0)

# Bottom UP
def shortestCommonSupersequence(str1: str, str2: str) -> str:
    str1_len,str2_len = len(str1), len(str2)

    dp = [[0  for _ in range(str2_len+1)] for _ in range(str1_len+1)]

    for i in range(str1_len+1):
        dp[i][0] = i

    for j in range(str2_len+1):
        dp[0][j] = j

    for i in range(1, str1_len+1):
        for j in range(1, str2_len+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1


    sequence_str = []
    row,col = str1_len,str2_len
    while row > 0 and col > 0:
        if str1[row-1] == str2[col-1]:
            sequence_str.append(str1[row-1])
            row -= 1
            col -= 1
        
        elif dp[row-1][col] < dp[row][col-1]:
            sequence_str.append(str1[row-1])
            row -= 1
        else:
            sequence_str.append(str2[col-1])
            col -= 1
    
    while row > 0:
        sequence_str.append(str1[row-1])
        row -= 1

    while col > 0:
        sequence_str.append(str2[col-1])
        col -= 1
    
    return "".join(sequence_str[::-1])

str1 = "bbabacaa"
str2 = "cccabababacaa"

print(shortestCommonSupersequence(str1, str2))