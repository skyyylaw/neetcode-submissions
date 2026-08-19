class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        S = sum(stones)
        dp = [False] * (S // 2 + 1)
        dp[0] = True
        
        firstSubsetSum = 0
        for s in stones:
            for i in range(len(dp) - 1, s - 1, -1):
                dp[i] = dp[i] or dp[i - s]
                if dp[i]:
                    firstSubsetSum = max(firstSubsetSum, i)
        
        return (S - firstSubsetSum) - firstSubsetSum
