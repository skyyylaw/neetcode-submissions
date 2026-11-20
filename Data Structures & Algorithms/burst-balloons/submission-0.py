from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        @cache
        def getCoins(i, arr):
            coins = 1
            coins *= arr[i-1] if i-1 >= 0 else 1
            coins *= arr[i]
            coins *= arr[i+1] if i+1 < len (arr) else 1
            return coins
        
        @cache
        def findOptimal(options):
            if not options:
                return 0
            maximum = 0
            for i in range(len(options)):
                coins = getCoins(i, options)
                maximum = max(maximum, coins + findOptimal(options[:i] + options[i+1:]))
            return maximum
        
        return findOptimal(tuple(nums))

