class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curr = 0
        for e in nums:
            if curr < 0:
                curr = 0
            curr += e
            ans = max(ans, curr)
        return ans