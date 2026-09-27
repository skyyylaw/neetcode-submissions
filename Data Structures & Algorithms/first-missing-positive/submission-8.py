class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            num = nums[i]
            numIndex = num - 1
            if nums[i] == numIndex:
                # in place
                i += 1
            else:
                # out of place
                if numIndex < 0 or numIndex >= len(nums):
                    # cannot fit
                    i += 1
                else:
                    # can fit
                    if nums[numIndex] != num:
                        nums[i], nums[numIndex] = nums[numIndex], nums[i]
                    else:
                        i += 1
        # print(nums)
        for i, n in enumerate(nums):
            if i != n - 1:
                return i + 1
        return len(nums) + 1
