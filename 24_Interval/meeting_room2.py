class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def minMeetingRooms(self, intervals: list[Interval]) -> int:
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()

        i,j=0,0
        n=len(intervals)

        result = 0
        count = 0
        while i < n and j < n:
            if start[i] >= end[j]:
                count -= 1
                j += 1
            elif start[i] < end[j]:
                count += 1
                result = max(count, result)
                i += 1

        return result

