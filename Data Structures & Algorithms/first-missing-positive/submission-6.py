class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = len(nums) - 1
        ans = len(nums)
        while i >= 0:
            num = nums[i]
            numIndex = num - 1
            if i == numIndex:
                # in place
                i -= 1
            else:
                # out of place
                ans = i
                if numIndex < 0 or numIndex >= len(nums):
                    # cannot fit
                    i -= 1
                else:
                    # can fit
                    if nums[numIndex] != num:
                        nums[i], nums[numIndex] = nums[numIndex], nums[i]
                    else:
                        i -= 1
        if nums[ans] == ans + 1:
            return len(nums)
        return ans + 1
