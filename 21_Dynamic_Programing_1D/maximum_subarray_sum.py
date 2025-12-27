

def maxProduct(nums: list[int]) -> int:
    curr_min,curr_max = 1,1
    res = nums[0]
    for num in nums:
        temp = curr_max*num

        curr_max = max(temp, num * curr_min, num)
        curr_min = min(temp, num * curr_min, num)
        res = max(res, curr_max)
    
    return res

nums = [2,3,-2,-4]

print(maxProduct(nums))