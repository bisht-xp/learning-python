def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x:x[0])
    n = len(intervals)
    i=0
    print("sorted Interval", intervals)
    result = []
    while i < n:
        newInterval = intervals[i]
        i+=1
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1

        result.append(newInterval)

    return result


intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
print(merge(intervals))