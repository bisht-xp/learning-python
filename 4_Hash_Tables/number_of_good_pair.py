def numIdenticalPairs( nums: list[int]) -> int:
    count_map = {}
    count = 0

    for num in nums:
        if num in count_map:
            count += count_map[num]
            count_map[num] += 1  
        else:  
            count_map[num] = 1
    
    return count

print(numIdenticalPairs([1,1,1,1]))