class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        # print(candidates)
        ans = []
        def search(i, sum_, combo):
            # print(sum_, combo)
            if sum_ == target:
                ans.append(combo.copy())
                return
            elif sum_ > target:
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j-1]: 
                    continue
                combo.append(candidates[j])
                search(j+1, sum_ + candidates[j], combo)
                combo.pop()
        search(0, 0, [])
        return ans