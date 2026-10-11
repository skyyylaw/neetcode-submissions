class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        maxSum = sum(nums)
        n = len(nums)
        dpRowLength = maxSum * 2 + 1
        
        prevRow = [0] * (dpRowLength)
        prevRow[len(prevRow) // 2] = 1
        nextRow = [0] * (dpRowLength)
        for r in range(n):
            for c in range(dpRowLength):
                if c - nums[r] >= 0:
                    nextRow[c] += prevRow[c - nums[r]]
                if c + nums[r] < dpRowLength:
                    nextRow[c] += prevRow[c + nums[r]]
            prevRow = nextRow
            nextRow = [0] * (dpRowLength)
        
        mid = dpRowLength // 2
        # print(prevRow)
        if mid + target < 0 or mid + target >= dpRowLength:
            return 0
        return prevRow[mid + target] 