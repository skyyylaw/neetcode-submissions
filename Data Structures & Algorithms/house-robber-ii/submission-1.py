class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])


        dp = [(0, False)] * n
        dp[0] = (nums[0], True)
        for i in range(1, n):
            if i-2 >= 0 and dp[i-1][0] > dp[i-2][0] + nums[i]:
                dp[i] = (dp[i-1][0], dp[i-1][1])
            else:
                dp[i] = (dp[i-2][0] + nums[i], dp[i-2][1])
        
        dp2 = [0] * n
        dp2[1] = nums[1]
        for i in range(2, n):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])

        # print(dp)
        # print(dp2)

        if not dp[-1][1]:
            return max(dp[-1][0], dp2[-1])
        return max(dp[-2][0], dp2[-1])

            