class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = 0
        count = 0
        for n in nums:
            if n == ele:
                count += 1
            else:
                count -= 1
                if count == -1:
                    ele = n
                    count = 1
        return ele