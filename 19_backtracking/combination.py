#  This is the pattern to solve other backtracking problem

def combine( n: int, k: int) -> list[list[int]]:
    result = []

    def helper(i, comb):
        if k == len(comb):
            result.append(comb.copy())
            return
        
        if i > n:
            return
        

        for j in range(i, n+1):
            comb.append(j)
            helper(j+1, comb)
            comb.pop()
    
    helper(1, [])
    return result


print(combine(5, 2))
