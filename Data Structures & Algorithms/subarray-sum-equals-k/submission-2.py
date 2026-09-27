class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = []
        counter = defaultdict(int)
        
        counter[0] = 1

        ans = 0
        
        for i, n in enumerate(nums):
            if not prefixSum:
                prefix = n
            else:
                prefix = n + prefixSum[-1]
            
            prefixSum.append(prefix)

            ans += counter[prefix - k]  
            
            counter[prefix] += 1
        
        
                  
        
        return ans
