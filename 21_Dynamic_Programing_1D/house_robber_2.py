def rob( nums: list[int]) -> int:
    # cache = {}
    # n = len(nums)
    # if n== 1:
    #     return nums[0]
    # def dfs(i, n):
    #     if i >= n:
    #         return 0
        
    #     if((i,n) in cache):
    #         return cache[i]
        
    #     left = dfs(i+1, n)
    #     right = nums[i] + dfs(i+2, n)
        
    #     cache[(i,n)] =  max(left, right)
    #     return cache[(i,n)]
    # return max(dfs(0, n-1), dfs(1, n))

    # Bottom UP Apporach

    if len(nums) == 1:
        return nums[0]
    
    def helper(newArr):
        if(not newArr):
            return 0
        
        if(len(newArr) == 1):
            return newArr[0]
        
        dp = [-1]*len(newArr)
        dp[0] = newArr[0]
        dp[1] = max(newArr[0], newArr[1])

        for i in range(2,len(newArr)):
            dp[i] = max(dp[i-1], dp[i-2] + newArr[i])

        return dp[len(newArr)-1]

    return max(helper(nums[1:]), helper(nums[:-1]));

nums = [1,2,3]
print(rob(nums))
    