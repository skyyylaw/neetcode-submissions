class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        counter = defaultdict(int)
        for e in candidates:
            counter[e] += 1
        

        memo = []
        for v, freq in counter.items():
            memo.append([v, freq])

        memo.sort()

        # print(memo)
        
        
        def search(i, currSum, combo):
            if currSum == target:
                ans.append(combo.copy())
                return
            if currSum > target:
                return
            
            for j in range(i, len(memo)):
                currSum += memo[j][0]
                combo.append(memo[j][0])
                memo[j][1] -= 1
                if memo[j][1] > 0:
                    search(j, currSum, combo)
                else:
                    search(j+1, currSum, combo)
                combo.pop()
                currSum -= memo[j][0]
                memo[j][1] += 1
        
        search(0, 0, [])
        return ans
            