def longestConsecutive( nums: list[int]) -> int:
    unique_ele = set(nums)
    ans = 0
    for num in unique_ele:
        print("nums: ", num)
        if num-1 not in unique_ele:
            ele = num
            count = 1
            while ele+1 in unique_ele:
                count += 1
                ele += 1
            ans = max(ans, count) 

    return ans


print(longestConsecutive([100,4,200,1,3,2]))
        