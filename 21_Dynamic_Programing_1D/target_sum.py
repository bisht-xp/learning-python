def findTargetSumWays( nums: list[int], target: int) -> int:
    n = len(nums)
    cache = {}
    def dfs(i, totalSum):
        if i >= n:
            return 1 if totalSum == target else 0
        
        if (i,totalSum) in cache:
            return cache[(i,totalSum)]
        
        cache[(i,totalSum)] = (dfs(i+1, totalSum+nums[i]) + dfs(i+1, totalSum - nums[i]))
        return cache[(i,totalSum)]
    return dfs(0, 0)



nums = [1,1,1,1,1]
target = 3

print(findTargetSumWays(nums, target))    