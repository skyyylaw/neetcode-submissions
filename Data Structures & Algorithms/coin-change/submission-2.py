class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for c in coins:
            if c < amount + 1:
                dp[c] = 1
        
        for i in range(1, amount):
            if dp[i] != float('inf'):
                for c in coins:
                    if i+c < amount + 1:
                        dp[i+c] = min(dp[i+c], dp[i] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
