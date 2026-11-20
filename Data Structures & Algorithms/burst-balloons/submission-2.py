from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        
        @cache
        def findOptimal(l, r):
            if l > r:
                return 0
            maximum = 0
            for i in range(l, r+1):
                maximum = max(maximum, 
                    (
                        findOptimal(l, i - 1) +
                        nums[i] * nums[l-1] * nums[r + 1] +
                        findOptimal(i+1, r)
                    )
                )
            return maximum
        return findOptimal(1, len(nums)-2)

