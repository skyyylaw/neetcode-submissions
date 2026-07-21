class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, e in enumerate(nums):
            if e != i+1:
                if nums[e-1] == e:
                    return e
                else:
                    nums[e-1], nums[i] = e, nums[e-1]
        