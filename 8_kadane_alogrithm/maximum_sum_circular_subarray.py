def maxSubarraySumCircular(nums: list[int]) -> int:
    current_max = 0
    current_min = 0
    global_max = nums[0]
    global_min = nums[0]
    total_sum=0

    for num in nums:
        total_sum += num
        # current_max = max(num, current_max+num)
        # current_min = min(num, current_min+num)
        if current_max < 0:
            current_max = 0
        current_max += num

        if current_min > 0:
            current_min = 0
        current_min += num
        global_max = max(global_max, current_max)
        global_min=min(global_min, current_min)
    
    if global_max < 0:
        return global_max

    return global_max if global_max > total_sum - global_min else total_sum -global_min

print(maxSubarraySumCircular([5,-3,5]))