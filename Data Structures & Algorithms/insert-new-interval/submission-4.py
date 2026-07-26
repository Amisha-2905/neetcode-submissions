class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        n = len(intervals)
        target = newInterval[0]
        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            if intervals[mid][0] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        intervals.insert(l, newInterval)

        i = l
        if i > 0 and intervals[i-1][1] >= intervals[i][0]:
            intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
            intervals.pop(i)
            i -= 1

        while i + 1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
            intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
            intervals.pop(i+1)

        return intervals


