class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        for e in intervals:
            if ans and ans[-1][1] >= e[0]:
                ans[-1][1] = max(ans[-1][1], e[1])
            else:
                ans.append(e)
        return ans