def subsets(nums: list[int]) -> list[list[int]]:
    subset,result=[],[]

    def helper(i,nums,subset, result):
        if i >= len(nums):
            subset.append(result.copy())
            return
        
        result.append(nums[i])
        helper(i+1, nums, subset, result)
        result.pop()
    
        helper(i+1, nums, subset, result)
    
    helper(0,nums,subset,result)

    return subset


print(subsets([1,2,3]))