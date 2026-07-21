class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefixMin = []
        ans = 0
        for i in range(len(prices)):
            p = prices[i]
            ans = max(ans, p - prefixMin[-1] if prefixMin else 0)
            if not prefixMin:
                prefixMin.append(p)
            else:
                prefixMin.append(min(p, prefixMin[-1]))
        return ans
                
        