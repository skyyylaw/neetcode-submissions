class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        # [4 5 6 1 2 3 ]
        while left <= right:
            mid = (left + right) // 2
            l, m, r = nums[left], nums[mid], nums[right]
            if nums[mid-1] >= m:
                return m
            if l < r:
                right = mid - 1
            else:
                if m < l:
                    right = mid - 1
                else:
                    left = mid + 1