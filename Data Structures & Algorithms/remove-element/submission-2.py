class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == val else 1
        right = len(nums) - 1
        valCount = 0
        for left in range(len(nums)):
            while nums[right] == val and right >= 0:
                valCount += 1
                right -= 1
            if nums[left] == val and  left < right:
                valCount += 1
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
        return len(nums) - valCount