def singleNumber(nums: list[int]) -> int:
    n = len(nums)
    
    if n == 1:
        return nums[0]
    
    single_number = nums[0]

    for i in range(1, n):
        single_number ^=  nums[i]
    
    return single_number


print(singleNumber([4,1,2,1,2]))