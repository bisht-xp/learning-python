def rotate(nums: list[int], k: int) -> None:
    n = len(nums)
    k = k % n
    if k == 0:
        return
    for i in range(n//2): 
        [nums[i], nums[n-1-i]] = [nums[n-1-i], nums[i]]
        i+= 1
    
    i = 0
    while i < k-1-i:
        [nums[i], nums[k-i-1]] = [nums[k-i-1], nums[i]]
        i += 1
    
    i = 0
    while k < n -1- i:
        [nums[k], nums[n-1-i]] = [nums[n-1-i], nums[k]]
        i += 1
        k += 1
    
    print("array: ", nums)
    




rotate([1,2,3,4,5,6], 1)
        

        
        