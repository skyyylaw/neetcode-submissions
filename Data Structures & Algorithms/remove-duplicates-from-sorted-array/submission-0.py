class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        prev = None
        for j in range(len(nums)):
            if prev != None and nums[j] != prev:
                nums[i] = nums[j]
                i+=1
            prev = nums[j]
        return i