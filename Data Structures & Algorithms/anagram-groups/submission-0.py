class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        for s in strs:
            sorted_strs.append("".join(sorted(s)))
        ans = defaultdict(list)
        for i in range(len(sorted_strs)):
            ans[sorted_strs[i]].append(strs[i])
        ans = [v for k, v in ans.items()]
        return ans