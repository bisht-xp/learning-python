def mincostTickets(days: list[int], costs: list[int]) -> int:
    valid_day = [0,6,29]

    # return dfs(0)
    n = len(days)

    dp = [0]*(n+1)

    for i in range(n-1, -1,-1):
        dp[i] = float('inf')
        for k in range(3):
            duration = valid_day[k]
            cost = costs[k]

            max_covered_days = days[i] + duration
            
            j = i
            while j < n and days[j] <= max_covered_days:
                j += 1
            
            include = cost + dp[j]
            dp[i] = min(dp[i], include)
    

    return dp[0]



days = [1,4,6,7,8,20]
costs = [2,7,15]
print(mincostTickets(days, costs))