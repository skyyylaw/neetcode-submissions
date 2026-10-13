class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        from functools import cache
        @cache
        def backtrack(i):
            res = False
            for word in wordDict:
                if word == s[i:]:
                    return True
                if word == s[i:i+len(word)]:
                    res = res or backtrack(i+len(word))
            return res
        return backtrack(0)
