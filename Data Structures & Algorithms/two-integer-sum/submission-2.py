class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = defaultdict(list)
        for i, e in enumerate(nums):
            indexes[e].append(i)
        for e in indexes:
            if target - e in indexes:
                if e == target - e:
                    if len(indexes[e]) >= 2:
                        return indexes[e][:2]
                    continue
                return [indexes[e][0], indexes[target-e][0]]
                