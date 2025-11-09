# first method of permuation using checking index and add the element if not in the dictionary.

# def permute( nums: list[int]) -> list[list[int]]:
#     result = []
#     n = len(nums)
#     def helper(ans,dic: dict):
#         if len(ans) == n:
#             result.append(ans.copy())
#             return
        
#         for i in range(n):
#             if nums[i] not in dic:
#                 ans.append(nums[i])
#                 dic[nums[i]] = True
#                 helper(ans, dic)
#                 del dic[nums[i]]
#                 ans.pop()
#     helper([], {})

#     return result




# This is swaping problem on there place is also good approch
def permute( nums: list[int]) -> list[list[int]]:
    result = []
    def helper(idx, nums):
        if idx == len(nums):
            result.append(nums.copy())
            return

        for i in range(idx, len(nums)):
            nums[i],nums[idx] = nums[idx],nums[i]
            helper(idx+1,nums)
            nums[i],nums[idx] = nums[idx],nums[i]

    helper(0,nums)
    return result


print(permute([1,1,3]))