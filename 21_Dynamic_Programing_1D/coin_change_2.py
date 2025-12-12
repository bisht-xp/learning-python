def change(amount: int, coins: list[int]) -> int:
    
    # def dfs(i, amount):
    #     if amount == 0:
    #         return 1
        
    #     if(i >= len(coins) or amount < 0):
    #         return 0
        
    #     if coins[i] <= amount:
    #         return dfs(i, amount-coins[i]) + dfs(i+1, amount)
    #     else:
    #         return dfs(i+1,amount)
    

    # return dfs(0, amount)
    n = len(coins)
    dp =  [[0 for _ in range(amount+1)] for _ in range(n + 1)]

    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, n+1):
        coin = coins[i-1]
        for j in range(1,amount+1):
            if coin <= j:
                dp[i][j] = dp[i][j-coin] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    
    
    return dp[n][amount]

amount = 5
coins = [1,2,5]

print(change(amount, coins))