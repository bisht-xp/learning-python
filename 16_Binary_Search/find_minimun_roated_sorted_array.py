def findMin(nums: list[int]) -> int:
    l,h=0,len(nums)-1

    while(l < h):
        mid = (l+h)//2

        if(nums[mid] > nums[h]):
            l=mid+1
        else:
            h=mid

    return nums[l]


print(findMin([4,5,6,7]))