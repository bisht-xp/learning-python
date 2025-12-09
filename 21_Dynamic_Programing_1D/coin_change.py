def coinChange(coins: list[int], amount: int) -> int:
    n = len(coins)
    dp = [[float('inf') for _ in range(amount+1)] for _ in range(n+1)]


    for i in range(n+1):
        dp[i][0] = 0
    

    for i in range(1, n+1):
        coin = coins[i-1]
        for j in range(1, amount+1):
            if coin <= j:
                dp[i][j] = min(1+ dp[i][j-coin], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
        
    
    return dp[n][amount] if dp[n][amount] != float('inf') else -1


coins = [2]
amount = 3

print(coinChange(coins, amount))