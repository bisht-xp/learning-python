def isHappy( n: int) -> bool:
    slow = n
    fast = get_next(n)
    while slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))
    
    return slow == 1




def get_next(n): 
    total = 0
    while n:
        num = n%10
        total += num*num
        n //=10
    
    return total


print(isHappy(19))