def longestOnes( nums: list[int], k: int) -> int:
    max_len=0
    left=0

    for right in range(len(nums)):
        if nums[right] == 0:
            k -= 1
        
        if k < 0:
            if nums[left] == 0:
                k += 1
            left += 1
        
        max_len = max(max_len, right-left+1)
    
    return max_len

print(longestOnes([0,0 ,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))