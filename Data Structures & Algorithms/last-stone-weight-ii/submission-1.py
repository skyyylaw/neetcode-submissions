class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        S = sum(stones)
        n = len(stones)

        dp = [[False] * (S//2 + 1) for _ in range(n+1)]

        dp[0][0] = True

        subsetSum = 0

        for i in range(len(dp)):
            for t in range(len(dp[i])):
                dp[i][t] = dp[i-1][t] or dp[i][t] 
                if t - stones[i-1] >= 0:
                    dp[i][t] = dp[i][t] or dp[i-1][t-stones[i-1]]
                if dp[i][t]:
                    subsetSum = max(subsetSum, t)

        return S - 2 * subsetSum


