def minSubArrayLen(target: int, nums: list[int]) -> int:
    total_sum = 0
    for num in nums:
        total_sum += num
    
    if target > total_sum: 
        return 0

    sum = 0
    min_len=len(nums)
    start=0
    for end in range(len(nums)):
        sum += nums[end]
        while sum >= target:
            min_len = min(min_len, end-start+1)
            sum -= nums[start]
            start += 1
        
    return min_len


print(minSubArrayLen(7,[2,3,1,2,4,3]))
