class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        sum = 0
        ans = len(nums)
        while r < len(nums):
            sum += nums[r]
            while sum >= target:
                ans = min(ans, r - l + 1)
                sum -= nums[l]
                l += 1
            r += 1
        return ans if ans != len(nums) else 0