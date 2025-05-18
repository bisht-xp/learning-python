def countBits(n: int) -> list[int]:
    if n == 0:
        return [0]
    if n == 1:
        return [0,1]
    ans = [0]*(n+1)
    ans[0],ans[1]=0,1

    for i in range(2, n+1):
        ans[i] = 1 + ans[i&(i-1)]
    

    return ans

print(countBits(16))