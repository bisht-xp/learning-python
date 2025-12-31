# def lengthOfLIS(nums: list[int]) -> int:
#     def dfs(i, prev):
#         if i >= len(nums):
#             return 0
        
#         if prev == -1 or nums[i] > nums[prev]:
#             return max(1 + dfs(i+1, i), dfs(i+1,prev))
#         else:
#             return dfs(i+1, prev)
    

#     return dfs(0,-1)

def lengthOfLIS(nums: list[int]) -> int:
    dp = [1]*len(nums)

    for i in range(1,len(nums)):
        for j in range(0, i):
            if(nums[i] > nums[j]):
                dp[i] = max(1+dp[j], dp[i])
    
    return max(dp)


nums = [0,1,0,3,2,3,4]
print(lengthOfLIS(nums))
