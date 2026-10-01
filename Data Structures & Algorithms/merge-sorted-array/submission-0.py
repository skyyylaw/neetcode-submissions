class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        
        x = m + n - 1
        while x >= 0:
            if i <0 or (j >= 0 and nums2[j] >= nums1[i]):
                nums1[x] = nums2[j]
                j -= 1
            else:
                nums1[x] = nums1[i]
                i -= 1
            x -= 1
