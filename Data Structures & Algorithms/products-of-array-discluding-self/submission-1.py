class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        
        prefix = [1] * n
        postfix = [1] * n
        
        for l in range(n):
            r = n - l - 1
            if l == 0:
                prefix[l] = nums[l]
                postfix[r] = nums[r]
            else:
                prefix[l] = nums[l] * prefix[l-1]
                postfix[r] = nums[r] * postfix[r+1]
        
        output = [0] * n

        for i in range(len(output)):
            if i == 0:
                output[i] = postfix[i+1]
            elif i == n - 1:
                output[i] = prefix[i-1]
            else:
                output[i] = prefix[i-1] * postfix[i + 1]
        
        return output
