def longestConsecutive(nums: list[int]) -> int:
    n = len(nums)
    ele = set(nums)
    ans = -1
    for e in ele:
        if e-1 not in e:
            val = e
            count = 1 
            while val+1 in ele:
                count += 1
                val += 1
            
            ans = max(ans, count)
    
    return ans



print(longestConsecutive([100,4,200,1,3,2,2,3,4]))