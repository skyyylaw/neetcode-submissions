class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(prices))]
        buyPrice = 0
        for i in range(1, len(dp)):
            for j in range(3):
                if j == 0:
                    # print("HOLD")
                    dp[i][j] = dp[i-1][1] - prices[i]
                elif j == 1:
                    # print("rest")
                    # the prev step could have been any of the three
                    dp[i][j] = max(dp[i-1])
                else:
                    # print("sell")
                    # the prev step can only be buy or rest
                    # need to calculate the profit
                    dp[i][j] = max(dp)
        