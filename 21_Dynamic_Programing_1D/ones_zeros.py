from collections import defaultdict


def findMaxForm(strs: list[str], m: int, n: int) -> int:
    
    memo = [[[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(strs) + 1)]
    
    # def dfs(i,m,n):
    #     if i >= len(strs):
    #         return 0

    #     zero, one = strs[i].count('0'),strs[i].count('1')
    #     right = -1
    #     if((i,m,n) in memo):
    #         return memo[(i,m,n)]
        
    #     if(m-zero >= 0 and n-one >= 0):
    #         right = 1 + dfs(i+1, m-zero,n-one)
        

    #     left = dfs(i+1, m,n)
    #     memo[(i,m,n)] =  max(left, right)
    #     return memo[(i,m,n)]
        

    # return dfs(0,m,n)

    for i  in range(1,len(strs)+1):
        s = strs[i-1]
        zero,one = s.count('0'),s.count('1')
        for j in range(m+1):
            for k in range(n+1):
                if j >= zero and k >= one:
                    include = 1 + memo[i-1][j-zero][k-one]
                    exclue = memo[i-1][j][k]
                    memo[i][j][k] = max(include, exclue)
                else:
                    memo[i][j][k] = memo[i-1][j][k]
    

    return memo[len(strs)][m][n]


strs = ["10","0001","111001","1","0"]
m = 4
n = 3
print(findMaxForm(strs,m,n))