def findDuplicate(nums: list[int]) -> int:
    n = len(nums)
    ans = []

    for i in range(n):
        num = abs(nums[i])
        if nums[num-1] < 0:
            ans.append(num)
        
        nums[num-1] = -abs(nums[num-1])

    return ans


print(findDuplicate([4,3,2,7,8,2,3,1]))   