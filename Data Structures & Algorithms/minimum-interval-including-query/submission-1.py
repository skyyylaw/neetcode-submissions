class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        dp = dict()
        for s, e in intervals:
            for i in range(s, e+1):
                if i not in dp:
                    dp[i] = e-s+1
                else:
                    dp[i] = min(dp[i], e - s + 1)
        ans = [dp[e] if e in dp else -1 for e in queries]
        return ans