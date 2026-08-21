class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 3 for _ in range(len(prices))]
        
        dp[0][0] = -prices[0]
        dp[0][2] = -100000000
        
        for i in range(1, len(dp)):
            
            # hold
            # 1) we bought
            # 2) we simply hold the last bought
            dp[i][0] = max(dp[i-1][1] - prices[i], dp[i-1][0])
                
            # rest
            # no holding rn
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])

            # sell
            # sell the prev holding
            dp[i][2] = dp[i-1][0] + prices[i]
        
        
        return max(dp[-1])
        