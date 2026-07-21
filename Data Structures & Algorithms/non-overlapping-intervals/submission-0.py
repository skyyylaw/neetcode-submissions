class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        final = []
        delete = 0
        intervals.sort()
        for e in intervals:
            if final and final[-1][1] > e[0]:
                # overlap
                delete += 1
                final[-1][1] = min(final[-1][1], e[1])
            else:
                final.append(e)
        return delete