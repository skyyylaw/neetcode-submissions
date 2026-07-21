class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mini = max(max(piles) // h, 1)
        maxi = max(piles)
        
        def canFinish(speed):
            return sum(math.ceil(e / speed) for e in piles) <= h
        
        res = None
        while mini <= maxi:
            mid = (mini + maxi) // 2
            if canFinish(mid):
                res = mid
                maxi = mid - 1
            else:
                mini = mid + 1
        
        return res
