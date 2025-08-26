def findPeakElement( nums: list[int]) -> int:
    l,r=0,len(nums)-1

    while(l < r):
        mid = (l+r)//2

        if(nums[mid] > nums[mid+1]):
            r = mid
        else:
            l = mid+1
    
    return l



print(findPeakElement([1,2]))         