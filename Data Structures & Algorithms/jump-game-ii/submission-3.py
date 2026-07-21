class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        reach = 0
        res = 0
        i = 0
        while reach < n-1:
            newReach = reach
            while i <= reach:
                if i + nums[i] > newReach:
                    newReach = max(newReach, i + nums[i])
                i += 1
            reach = newReach
            res +=1 
        return res
