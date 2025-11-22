def rob( nums: list[int]) -> int:
    result = [0]*(len(nums)+1)
    # def dfs(i):
    #     if i >= len(nums):
    #         return 0
        
    #     if i in result:
    #         return result[i]
    #     left = dfs(i+1)
    #     right = nums[i] + dfs(i+2)
    #     result[i] =  max(left, right)
    #     return result[i]
    
    # return dfs(0)
    for i in range(len(nums)):
        result[i] = max(result[i-1], nums[i] + result[i-2])
    
    print(result)
    return result[len(nums)]

print(rob([2,1,1,2]))