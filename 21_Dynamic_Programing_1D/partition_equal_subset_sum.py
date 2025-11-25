def canPartition(nums: list[int]) -> bool:
    if sum(nums)%2 != 0:
        return False

    target = sum(nums)//2
    n = len(nums)+1
    memo =  [[False] * (target + 1) for _ in range(n)]
    
    for i in range(n):
        memo[i][0] = True
            
    for i in range(1, n):
        for j in range(1, target+1):
            if nums[i-1] <= j:
                memo[i][j] = (memo[i-1][j-nums[i-1]] or memo[i-1][j])
            else:
                memo[i][j] = memo[i-1][j]

    
    
    for i in range(n):
        print(memo[i])
    return memo[n][target]

nums = [1,5,11,5]
print(canPartition(nums))