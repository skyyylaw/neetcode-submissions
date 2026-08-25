class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        nums = []
        for i in range(1, len(dp)):
            if (math.sqrt(i) % 1 == 0):
                dp[i] = 1
                nums.append(i)
                continue
            for n in nums:
                dp[i] = min(dp[i], dp[i - n] + 1)
        return int(dp[-1])
