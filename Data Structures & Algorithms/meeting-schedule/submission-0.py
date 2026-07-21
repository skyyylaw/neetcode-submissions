"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        prev = None
        intervals.sort(key = lambda x : x.start)
        for e in intervals:
            if prev and prev.end > e.start:
                return False
            prev = e
        return True