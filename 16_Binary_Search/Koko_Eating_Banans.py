import math

def minEatingSpeed(piles: list[int], h: int) -> int:
    def fesiable(speed):
        add = 0
        for pile in piles:
            add += math.ceil(pile/speed)
        
        return add <= h
    
    left,right=1,max(piles)

    while left < right:
        mid = (left+right)//2
        if fesiable(mid):
            right = mid
        else:
            left = mid+1

    return left


print(minEatingSpeed([3,6,7,11], 8))