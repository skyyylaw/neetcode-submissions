"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        days = 1
        intervals.sort(key = lambda x : x.start)
        prev = None
        for e in intervals:
            if prev and prev.end > e.start:
                days += 1
                prev.end = max(prev.end, e.end)
            else:
                prev = e
        return days
                