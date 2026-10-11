class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        start = 0
        accumulate = 0
        ans = 0
        for i, n in enumerate(nums):
            accumulate += n
            ans = max(ans, accumulate)
            if accumulate < 0:
                start = i + 1
            accumulate = max(0, accumulate)
        for i in range(start):
            n = nums[i]
            accumulate += n
            ans = max(ans, accumulate)
            accumulate = max(0, accumulate)
        

        return ans