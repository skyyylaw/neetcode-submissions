class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        start = -1
        accumulate = 0
        ans = 0
        for i in range(2*len(nums)):
            # print(i, start)
            if i % len(nums) == start:
                break
            if accumulate == 0:
                start = i
            n = nums[i % len(nums)]
            accumulate += n
            ans = max(ans, accumulate)
            accumulate = max(0, accumulate)
            
        return ans