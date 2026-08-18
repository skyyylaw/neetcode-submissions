class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
        def find(i, t):
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
            


            
            