class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(start, path, curr_sum):
            if curr_sum == target:
                ans.append(path.copy())
                return
            if curr_sum > target:
                return
            for i in range(start, len(nums)):
                n = nums[i]
                path.append(n)
                curr_sum += n
                dfs(i, path, curr_sum)
                path.pop(-1)
                curr_sum -= n
        dfs(0, [], 0)
        return ans