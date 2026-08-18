class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        prefixSum = []
        for e in nums:
            if not prefixSum:
                prefixSum.append(e)
            else:
                prefixSum.append(e + prefixSum[-1])

        def find(i, t):
            if abs(prefixSum[i]) < abs(t):
                return 0
            if (i, t) in cache:
                return cache[(i, t)]
            if i == 0:
                if t == nums[0] and -t == nums[0]:
                    return 2
                elif t == nums[0] or -t == nums[0]:
                    return 1
                return 0
            res = find(i - 1, t - nums[i]) + find(i-1, t + nums[i])
            cache[(i, t)] = res
            return res

        return find(len(nums)-1, target)
            


            
            