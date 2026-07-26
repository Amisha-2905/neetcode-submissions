"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        intervals.sort(key = lambda i: i.start)
        for i in range(len(intervals)):
            if rooms and rooms[0] <= intervals[i].start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i].end)
        return len(rooms)
        