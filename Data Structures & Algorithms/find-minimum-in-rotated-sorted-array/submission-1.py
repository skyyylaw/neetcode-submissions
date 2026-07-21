class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            left, right, mid = nums[l], nums[r], nums[m]
            if (m - 1 < 0 or nums[m-1] > mid) and (m + 1 >= len(nums) or mid < nums[m+1]):
                return mid
            if mid > right:
                l = m + 1
            else:
                r = m - 1