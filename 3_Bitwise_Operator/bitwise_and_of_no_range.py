def rangeBitwiseAnd( left: int, right: int) -> int:
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    
    ans = left << shift
    return ans
    

print(rangeBitwiseAnd(4,7))