class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maxi = 0
        ans = 0
        for e in nums:
            ans = ans ^ e
            maxi = max(maxi, e)
        for e in range(maxi+1):
            ans = ans ^ e
        return ans