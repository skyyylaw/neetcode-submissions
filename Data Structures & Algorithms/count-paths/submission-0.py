class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):
            dp.append([0] * n)
        dp[0][0] = 1
        for r in range(m):
            for c in range(n):
                if r-1 >= 0:
                    dp[r][c] += dp[r-1][c]
                if c-1 >= 0:
                    dp[r][c] += dp[r][c-1]
        return dp[-1][-1]