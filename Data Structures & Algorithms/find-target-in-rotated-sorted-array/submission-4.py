class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            
            mid = (left + right) // 2

            

            if nums[mid] == target:
                return mid
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right

            mid_in_left = False
            if nums[left] <= nums[mid] and nums[mid] > nums[right]:
                mid_in_left = True
            else:
                mid_in_left = False

            print(left, mid, right, mid_in_left)
            
            if nums[mid] < target:
                if mid_in_left:
                    left = mid + 1
                else:
                    if target > nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1
            else:
                if mid_in_left:
                    if target > nums[left]:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    right = mid - 1
        
        return -1