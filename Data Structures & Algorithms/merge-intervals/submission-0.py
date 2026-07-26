class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        while (i < len(intervals)):
            if i > 0 and intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
                i -= 1

            while i + 1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
            
            i += 1

        return intervals