class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        def solve(combo, options):
            if not options:
                ans.append(combo.copy())
            for i in range(len(options)):
                combo.append(options[i])
                solve(combo, options[:i] + options[i+1:])
                combo.pop()
        solve([], nums)
        return ans