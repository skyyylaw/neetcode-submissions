class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import cache

        @cache
        def search(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0
            res = 0
            if text1[i1] == text2[i2]:
                res = search(i1+1, i2+1) + 1
            res = max(res, search(i1+1, i2), search(i1, i2+1))
            return res

        return search(0,0)