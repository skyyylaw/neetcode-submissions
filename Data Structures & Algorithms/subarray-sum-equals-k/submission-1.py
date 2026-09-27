class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = []
        counter = defaultdict(int)
        
        counter[0] = 1
        
        for i, n in enumerate(nums):
            if not prefixSum:
                prefix = n
            else:
                prefix = n + prefixSum[-1]
            
            prefixSum.append(prefix)
            
            counter[prefix] += 1
        
        ans = 0

        # print(prefixSum)

        for i in range(len(prefixSum)-1, -1, -1):
            counter[prefixSum[i]] -= 1    
            ans += counter[prefixSum[i] - k]  
                  
        
        return ans
