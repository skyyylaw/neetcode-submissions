class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()

        candidates.sort()
        
        def search(i, currSum, combo):
            if currSum == target:
                ans.add(tuple(combo))
                return
            if currSum > target:
                return
            
            for j in range(i, len(candidates)):
                currSum += candidates[j]
                combo.append(candidates[j])
                search(j+1, currSum, combo)
                combo.pop()
                currSum -= candidates[j]
        
        search(0, 0, [])
        ans = list(ans)
        ans = [list(e) for e in ans]
        return ans
            