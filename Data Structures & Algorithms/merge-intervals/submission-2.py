class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        for each in intervals:
            if merged and merged[-1][1] >= each[0]:
                merged[-1][1] = max(merged[-1][1], each[1])
            else:
                merged.append(each)
        return merged