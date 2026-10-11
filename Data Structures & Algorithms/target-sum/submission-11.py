class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        maxSum = sum(nums)
        
        dp = [[0] * (maxSum * 2 + 1) for _ in range(len(nums)+1)]

        dp[0][len(dp[-1]) // 2] = 1

        for r in range(1, len(dp)):
            for c in range(len(dp[r])):
                if c - nums[r-1] >= 0:
                    dp[r][c] += dp[r-1][c-nums[r-1]] 
                if c + nums[r-1] < len(dp[r-1]):
                    dp[r][c] += dp[r-1][c+nums[r-1]]
        
        mid = len(dp[-1]) // 2
        if mid + target < 0 or mid + target >= len(dp[-1]):
            return 0
        return dp[-1][mid + target] 
            
