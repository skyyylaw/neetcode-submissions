class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        dp = [float('inf')] * 1000
        for s, e in intervals:
            for i in range(s, e+1):
                dp[i] = min(dp[i], e - s + 1)
        ans = [dp[e] if dp[e] != float('inf') else -1 for e in queries]
        return ans