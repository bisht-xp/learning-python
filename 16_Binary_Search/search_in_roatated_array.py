def search( nums: list[int], target: int) -> int:
    left,right = 0,len(nums)-1

    while(left <= right):
        mid = (left+right)//2

        if(nums[mid] == target) :
            return mid
        
        elif(nums[mid] >= nums[left]):
            if(nums[left] <= target < nums[mid]):
                right = mid
            else:
                left = mid+1
        else:
            if(nums[mid] < target <= nums[right]):
                left = mid+1
            else:
                right = mid

    return -1

nums,target = [1],1

print(search(nums, target))