class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        ans = []
        left = 0
        right = k - 1
        for i in range(k):
            counter[nums[i]] += 1
        
        ans.append(max(counter))

        while right < len(nums) - 1:
            counter[nums[left]] -= 1
            if counter[nums[left]] == 0:
                counter.pop(nums[left])
            left += 1
            
            right += 1
            counter[nums[right]] += 1
            ans.append(max(counter))

            
        return ans