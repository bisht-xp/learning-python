def reverseBits(n: int) -> int:
    result = 0
    for i in range(32):
        result <<= 1
        result |= n & 1
        n >>= 1
    return result

print(reverseBits(11111111111111111111111111111101))