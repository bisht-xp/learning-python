import math

def condition(piles, h, mid) -> bool:
    speed = 0
    for p in piles:
        speed += math.ceil(p/mid)
        if(speed > h) :
            return False
    return speed <= h


def minEatingSpeed(piles: list[int], h: int) -> int:
    lo,hi=min(piles),max(piles)
    
    while(lo <= hi):
        mid = (lo+hi)//2

        if(condition(piles,h,mid)) :
            hi = mid-1
        else:
            lo=mid+1

    return lo


piles = [1,4,3,2]
h = 9
print(minEatingSpeed(piles, h))