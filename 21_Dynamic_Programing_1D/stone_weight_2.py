from collections import defaultdict
from math import ceil


# def lastStoneWeightII(stones: list[int]) -> int:
#     stoneSum = sum(stones)
#     target = ceil(stoneSum/2)

#     memo = defaultdict(int)

#     def dfs(i, total):
#         if(total >= target or i >= len(stones)):
#             return abs(total - (stoneSum-total))
        
#         if (i,total) in memo:
#             return memo[((i, total))];

#         memo[(i, total)] = min(dfs(i+1, total), dfs(i+1, total+stones[i]))
#         return memo[(i, total)]

#     return dfs(0,0)


def lastStoneWeightII(stones: list[int]) -> int:
    stoneSum = sum(stones)
    target = stoneSum//2

    memo = [[False for _ in range(target+1)] for _ in range(len(stones)+1)]
    
    for i in range(len(stones)+1):
        memo[i][0] = True

    for i in range(1,len(stones)+1):
        for j in range(1,target+1):
            if stones[i-1] <= j:
                memo[i][j] = memo[i-1][j] or memo[i-1][j-stones[i-1]] 
            else:
                memo[i][j] = memo[i-1][j]

    n = len(stones)
    ans = 0
    for s1 in range(target, -1,-1):
        if(memo[n][s1] == True):
            ans = s1
            break
    
    return stoneSum - (2 * ans)

    


stones = [1,2,7]

print(lastStoneWeightII(stones))