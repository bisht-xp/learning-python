def containsNearbyDuplicate( nums: list[int], k: int) -> bool:
    hash_map = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in hash_map:
            if abs(i-hash_map[nums[i]]) <= k:
                return True
        
        hash_map[nums[i]] = i
    
    return False


print(containsNearbyDuplicate([1,2,3,1,2,3], 2))