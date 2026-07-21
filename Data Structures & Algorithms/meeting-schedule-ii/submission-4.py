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
        intervals = [[e.start, e.end] for e in intervals]
        memo = [] # heap
        for e in intervals:
            if memo and memo[0][0] <= e[0]:
                temp = heapq.heappop(memo)
                temp[0] = e[1]
                heapq.heappush(memo, temp)
            else:
                heapq.heappush(memo, e[::-1])
        return len(memo)
                