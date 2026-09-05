class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        arraySum = 0
        maxNum = -float('inf')
        runningSum = 0
        maxSum = 0
        for e in nums:
            arraySum += e
            maxNum = max(maxNum, e)
            runningSum = max(0, runningSum)
            runningSum += e
            maxSum = max(maxSum, runningSum)
        runningSum = 0
        minSum = 0
        for e in nums:
            runningSum = min(0, runningSum)
            runningSum += e
            minSum = min(minSum, runningSum)
        if maxSum == 0:
            return maxNum
        return max(maxSum, sum(nums) - minSum)