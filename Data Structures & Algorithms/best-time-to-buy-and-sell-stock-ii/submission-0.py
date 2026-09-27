class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for p in prices:
            buy = min(p, buy)
            if p > buy:
                profit += p - buy
                buy = p
        return profit