class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * (n)
        prefix = 1
        for i in range(n):
            prefix *= nums[i]
            output[i] = prefix
        postfix = 1
        for i in range(n-1, -1, -1):
            if i == 0:
                output[i] = postfix
            else:
                output[i] = output[i-1] * postfix
                postfix *= nums[i]
        return output