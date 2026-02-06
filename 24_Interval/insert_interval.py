def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    newList = []
    i = 0
    n= len(intervals)
    while i < n and intervals[i][1] < newInterval[0]:
        newList.append(intervals[i])
        i+= 1

    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval = min(intervals[i][0], newInterval[0])
        newInterval = max(intervals[i][1], newInterval[1])
        i += 1
    
    newList.append([newInterval, newInterval])
    
    while i < n:
        newList.append(intervals[i])
        i+=1

    return newList

print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
