class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = 0
        prevMax = 0
        prevMin = 0

        for i in range(len(nums)):
            if i == 0:
                prevMax = nums[0]
                prevMin = nums[0]
                ans = prevMax
                continue

            temp = max(prevMin*nums[i], prevMax*nums[i], nums[i])
            prevMin = min(prevMin*nums[i], prevMax*nums[i], nums[i])
            prevMax = temp
            ans = max(ans, prevMax, prevMin)

        return ans