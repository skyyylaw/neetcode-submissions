class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        reach = 0
        res = 0
        for i in range(n):
            r = i + nums[i]
            if r > reach:
                res += 1
                reach = r
            if reach >= n-1:
                return res 
