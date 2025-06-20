def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    ans = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
                continue
        j = i+1
        k = n-1
        while j < k:
            sum = nums[i] + nums[j] + nums[k]
            if sum == 0:
                ans.append([nums[i], nums[j], nums[k]])
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                while j < k and nums[j] == nums[j+1]:
                    j+=1
                k -= 1
                j += 1
            elif sum > 0:
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
                k -= 1
            else:
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                j += 1

    return ans

print(threeSum([-1,0,1,2,-1,-4]))
