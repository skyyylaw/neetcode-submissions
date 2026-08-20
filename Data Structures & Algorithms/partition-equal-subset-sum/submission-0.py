class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2 != 0:
            return False
        target = S // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for i in range(len(dp)-1, n-1, -1):
                dp[i] = dp[i] or dp[i-n]
        return dp[-1]