def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    subsets,res=[],[]
    nums.sort()
    def helper(i):
        if i >= len(nums):
            subsets.append(res.copy())
            return
        
        res.append(nums[i])
        helper(i+1)
        res.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i += 1
        
        helper(i+1)

    helper(0)
    return subsets

print(subsetsWithDup([1,2,2]))