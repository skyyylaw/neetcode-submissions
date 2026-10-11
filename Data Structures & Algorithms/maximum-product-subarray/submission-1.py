class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [0] * n
        for i in range(n):
            dp[i] = max(nums[i], dp[i-1]*nums[i]) if i-1 >= 0 else nums[i]
        return max(dp)