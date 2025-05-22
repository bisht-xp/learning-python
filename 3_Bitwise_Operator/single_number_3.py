def singleNumber(nums: list[int]) -> list[int]:
    xor_all = 0
    
    for i in nums:
        xor_all ^= i
    
    right_most_bit = xor_all & -xor_all

    a,b=0,0

    for i in nums:
        if right_most_bit & i:
            a ^= i
        else:
            b ^= i
    

    return [a,b]

print(singleNumber([-1,0]))