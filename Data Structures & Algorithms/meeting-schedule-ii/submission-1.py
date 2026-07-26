"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda i: i.start)
        if len(intervals) == 0:
            return 0
        rooms = [intervals[0].end]
        for i in range(1, len(intervals)):
            assigned = 0
            for j in range(len(rooms)):
                if intervals[i].start >= rooms[j]:
                    assigned = 1
                    rooms[j] = intervals[i].end
                    break
            if assigned == 0:
                rooms.append(intervals[i].end)

        return len(rooms)
        