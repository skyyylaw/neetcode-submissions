class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        intervals.append(newInterval)
        intervals.sort()
        for i in intervals:
            if ans and ans[-1][1] >= i[0]:
                ans[-1][1] = max(ans[-1][1], i[1])
                continue
            ans.append(i)
        return ans

