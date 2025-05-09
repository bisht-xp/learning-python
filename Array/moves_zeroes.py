def moveZeroes( nums: list[int]) -> None:
    n = len(nums)
    # i,j=0,0
    # while j < n:
    #     if nums[j] == 0 and nums[i] != 0:
    #         i = j
        
    #     if nums[i] == 0 and nums[j] != 0:
    #         nums[i],nums[j] = nums[j],nums[i]
    #         i += 1
        
    #     j += 1
    insertIndex = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[insertIndex],nums[i] = nums[i],nums[insertIndex]
            insertIndex += 1



moveZeroes([1,2,0,0,3,2,0])