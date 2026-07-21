class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        thres = len(nums) // 3
        counter = defaultdict(int)
        res = set()
        for e in nums:
            counter[e] += 1
            if counter[e] > thres:
                res.add(e)
        return list(res)