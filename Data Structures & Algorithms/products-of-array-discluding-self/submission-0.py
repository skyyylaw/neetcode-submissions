class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        non_zero_prod = 1
        zeroes = 0
        for e in nums:
            if e != 0:
                non_zero_prod *= e
            else:
                zeroes += 1
        for i, e in enumerate(nums):
            if zeroes and e != 0:
                nums[i] = 0
            elif zeroes > 1 and e == 0:
                nums[i] = 0
            elif zeroes == 1 and e == 0:
                nums[i] = non_zero_prod
            else:
                nums[i] = int(non_zero_prod / e)
        return nums