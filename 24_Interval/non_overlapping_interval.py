def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    stack = []
    i = 0
    count = 0
    for first,second in intervals:
        if not stack:
            stack.append([first, second])
            i += 1      
        else:
            [f, s] = stack[i-1]
            if s > first:
                count += 1
                if s > second:
                    stack.pop()
                    stack.append([first, second])
            else:
                stack.append([first, second])
                i += 1

    return count


print(eraseOverlapIntervals([[1,2],[2,3]]))


