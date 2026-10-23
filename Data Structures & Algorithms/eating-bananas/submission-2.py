class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(speed):
            return sum([math.ceil(e/speed) for e in piles]) <= h
        low = max(max(piles) // h, 1)
        high = max(piles)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if valid(mid):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans
