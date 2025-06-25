def findMaxAverage( nums: list[int], k: int) -> float:
    n = len(nums)
    i,j=0,0
    ans = float('-inf')
    totalCount = k
    sum = 0
    while j < n:
        sum += nums[j]
        k -=1
        if k == 0:
            totalSum = round(sum/totalCount,5)
            ans = max(ans, totalSum)
            sum -= nums[i]
            i += 1
            k += 1
        
        j += 1
    
    return round(ans, 5)

print(findMaxAverage([3], 1))