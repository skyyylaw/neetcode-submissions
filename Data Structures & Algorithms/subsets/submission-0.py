class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for i in range(len(nums)):
            new = []
            for e in ans:
                new.append(e + [nums[i]])
            ans += new
        return ans
