class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        options = set(nums)
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr.copy())
                return
            for e in options.copy():
                curr.append(e)
                options.remove(e)
                backtrack(curr)
                options.add(e)
                curr.pop()
        backtrack([])
        return ans