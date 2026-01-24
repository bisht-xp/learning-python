def maxProfit(prices: list[int]) -> int:
    n = len(prices)
    ans = 0
    i,j=0,0

    while j < n:
        ans = max(ans, prices[j]-prices[i])
        
        while i < n and prices[i] > prices[j]:
            i += 1
        
        j += 1
        
    
    return ans

print(maxProfit([7,6,4,3,1]))