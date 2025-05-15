def hammingWeight(n: int) -> int:
    count = 0
    while n > 0:
        count += n & 1
        n >>= 1
    
    return count

print(hammingWeight(2147483645))

