# def maximumSubarraySum( nums: list[int], k: int) -> int:
#     i,j=0,0
#     n=len(nums)
#     map_dict = {}

#     result,sum=0,0
#     while j < n:
#         while nums[j] in map_dict and map_dict[nums[j]] >= 1:
#             map_dict[nums[i]] -= 1
#             sum -= nums[i]
#             i += 1
#             k += 1
        
#         map_dict[nums[j]] = 1
#         sum += nums[j]
#         k -= 1
#         j += 1
#         if k == 0:
#             result = max(result, sum)
#             map_dict[nums[i]] -= 1
#             sum -= nums[i]    
#             i += 1
#             k += 1
    
#     return result

# trying to solve the problem with other methods
def maximumSubarraySum( nums: list[int], k: int) -> int:
    begin,end=0,0
    current_sum=0
    result=0
    num_last_index={}

    while end < len(nums):
        currNum = nums[end]
        last_occurrence = num_last_index.get(currNum, -1)

        while begin <= last_occurrence or end - begin + 1 > k:
            current_sum -= nums[begin]
            begin += 1

        current_sum += nums[end]
        num_last_index[nums[end]] = end

        if end - begin + 1 == k:
            result = max(result, current_sum)

        end += 1

    return result        



print(maximumSubarraySum([1,1,1,7,8,9], 3))