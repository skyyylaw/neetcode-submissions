class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
            
        dp = [0] * (amount+1)
        for c in coins:
            if c < amount + 1:
                dp[c] = 1
        for i in range(1, amount+1):
            if dp[i] > 0:
                for c in coins:
                    if i+c < amount + 1:
                        dp[i+c] += 1
        return dp[-1] if dp[-1] != 0 else -1
