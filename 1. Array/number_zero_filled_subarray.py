def zeroFilledSubarray( nums: list[int]) -> int:
    n = len(nums)
    i = 0
    ans = 0
    while i < n:
        count = 0
        while i < n and nums[i] == 0:
            count += 1
            i += 1
        if count > 0:
            ans += (count*(count+1))//2
        
        i += 1
    
    return ans


print(zeroFilledSubarray([1,3,0,0,2,0,0,4]))