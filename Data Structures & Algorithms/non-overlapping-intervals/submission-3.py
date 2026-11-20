class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[1])
        prev = []
        ans = 0
        for e in intervals:
            if prev and prev[1] > e[0]:
                ans += 1
                continue
            prev = e
        return ans


"""
[1 2] [1 4] [2 4]

"""