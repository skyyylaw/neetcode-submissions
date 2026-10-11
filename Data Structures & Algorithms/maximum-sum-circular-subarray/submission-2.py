class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ans = 0
        subarrayStart = 0
        subarraySum = 0
        for i, v in enumerate(nums):
            if subarraySum <= 0:
                subarrayStart = i
                subarraySum = 0
            subarraySum += v
            ans = max(ans, subarraySum)
        for i in range(subarrayStart):
            v = nums[i]
            if subarraySum <= 0:
                subarrayStart = i
                subarraySum = 0
            subarraySum += v
            ans = max(ans, subarraySum)
        return ans
            
            
