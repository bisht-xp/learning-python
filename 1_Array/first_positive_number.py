def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        # moving all the positive integer to the start then negative
        for i in range(n):
            if nums[i] > 0:
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
        
        # marking nums[i] to its indexes with reverse of that number
        for i in range(k):
            num = abs(nums[i])
            if num <= k:
                nums[num-1] = -abs(nums[num-1])
        
        for i in range(k):
            if nums[i] > 0:
                return i+1
        
        return k+1