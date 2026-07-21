class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            target = -nums[i]
            l = i+1
            r = n-1
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
        return [list(e) for e in ans]