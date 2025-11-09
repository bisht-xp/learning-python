from collections import Counter

def permuteUnique( nums: list[int]) -> list[list[int]]:
    result = []
    nums.sort()
    def helper(perm, counter):
        if len(perm) == len(nums):
            result.append(perm.copy())
            return
        
        for n in counter:
            if counter[n] > 0:
                perm.append(n)
                counter[n] -= 1
                helper(perm, counter)
                counter[n] += 1
                perm.pop()
        
    

    helper([],Counter(nums))

    return result


print(permuteUnique([1,2,3]))
