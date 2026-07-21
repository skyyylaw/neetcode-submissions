class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memo = set(nums)
        visited = set()
        ans = 0
        for e in nums:
            if e in visited:
                continue
            curr = 0
            while e in memo:
                curr += 1
                visited.add(e)
                e += 1
            ans = max(ans, curr)
        return ans