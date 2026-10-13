class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import cache
        @cache
        def backtrack(i):
            if i == len(s): 
                return True
            res = False
            for word in wordDict:
                if word == s[i:i+len(word)]:
                    res = res or backtrack(i+len(word))
            return res
        return backtrack(0)
