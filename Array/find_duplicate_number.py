def findDuplicate(nums: list[int]) -> int:
    n = len(nums)

    for i in range(n):
        num = abs(nums[i])
        if nums[num-1] < 0:
            return num
        
        nums[num-1] = -abs(nums[num-1])



print(findDuplicate([3,3,3,3,3]))    