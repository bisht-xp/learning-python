# solution 1
# def increasingTriplet(nums: list[int]) -> bool:
#         # this intiutive approdch where we are maintaining two array
#         n = len(nums)
#         small, large = [nums[0]]*n,[nums[n-1]]*n

#         # smallest element from the left in the small array
#         # largest element from the right 
#         for i in range(1,n):
#             small[i] = min(small[i-1], nums[i])
#             large[n-1-i] = max(large[n-i], nums[n-1-i])
        
#         # then compare current element check the smallest and largest then  answer it
#         for i in range(1,n-1):
#             if small[i-1] < nums[i] < large[i+1]:
#                  return True

#         return False

import sys

def increasingTriplet(nums: list[int]) -> bool: 
    n1, n2 = sys.maxsize, sys.maxsize

    for num in nums:
        if num < n2:
            return True
        if num <= n1:
            n1 = num
        elif num <= n2:
            n2 = num


    return False