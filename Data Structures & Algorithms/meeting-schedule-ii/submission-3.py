"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x : x.start)
        memo = []
        for e in intervals:
            if memo and memo[-1].end <= e.start:
                memo[-1].end = e.end
            else:
                memo.append(e)
        return len(memo)
                