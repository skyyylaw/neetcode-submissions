class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        ans = float('inf')
        while i < len(nums):
            num = nums[i]
            numIndex = num - 1
            if i == numIndex:
                # in place
                ans = i + 1
                i += 1
            else:
                # out of place
                ans = min(ans, i)
                if numIndex < 0 or numIndex >= len(nums):
                    # cannot fit
                    i += 1
                else:
                    # can fit
                    if nums[numIndex] != num:
                        nums[i], nums[numIndex] = nums[numIndex], nums[i]
                    else:
                        i += 1
        return ans + 1
