class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        
        curr = [e-1 for e in target]
        
        for t in triplets:
            pass_ = False
            for i in range(3):
                if t[i] > target[i]:
                    pass_ = True
            if pass_:
                continue
            for i in range(3):
                curr[i] = max(curr[i], t[i])
        
        return curr == target