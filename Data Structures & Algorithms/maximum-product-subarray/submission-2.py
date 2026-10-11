class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        firstNegIndex = -1
        lastNegIndex = -1

        allProd = 1
        for i, e in enumerate(nums):
            allProd *= e
            if e < 0 and firstNegIndex == -1:
                firstNegIndex = i
            if e <0:
                lastNegIndex = i
        
        ans = 0
        
        temp = allProd
        for i in range(firstNegIndex+1):
            temp /= nums[i]
        ans = max(ans, temp)
        temp = allProd
        for i in range(len(nums)-1, lastNegIndex-1, -1):
            temp /= nums[i]
        ans = max(ans, temp)

        return int(ans)
