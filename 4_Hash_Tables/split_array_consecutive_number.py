from collections import defaultdict

def isPossible( nums: list[int]) -> bool:
    freq = defaultdict(int)
    for num in nums:
        freq[num]+=1

    need = defaultdict(int)
    for num in nums:
        if freq[num] == 0:
            continue
        if num in need and need[num] > 0:
            need[num]-=1
            freq[num] -= 1
            need[num+1] += 1
        elif freq[num+1] > 0 and freq[num+2] > 0:
            freq[num] -= 1
            freq[num+1] -=1
            freq[num+2] -=1
            need[num+3] += 1
        else:
            return False 

    return True

print(isPossible([1,2,3,3,4,4,5,5]))