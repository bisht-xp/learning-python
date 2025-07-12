def maxProduct(nums: list[int]) -> int:
    max_prod = nums[0] 
    curr_max = curr_min = 1
    
    for num in nums:
        candidates = (num, curr_max * num, curr_min * num)
        curr_max = max(candidates)
        curr_min = min(candidates)
        
        max_prod = max(max_prod, curr_max)
    
    return max_prod

print(maxProduct([-2,-3,-4,0]))