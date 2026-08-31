class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # recursion solution

        dp = {}

        def recurse(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            res = float('inf')
            if i < 0 and j < 0:
                res = 0
            elif j < 0:
                res = i + 1
            elif i < 0:
                res = j + 1
            elif word1[i] == word2[j]:
                res = recurse(i-1, j-1)
            else:
                # delete
                res = min(res, recurse(i-1, j)+1)
                # insert
                res = min(res, recurse(i, j-1)+1)
                # replace
                res = min(res, recurse(i-1, j-1)+1)
            
            dp[(i, j)] = res
            return int(res)
        
        return recurse(len(word1)-1, len(word2)-1)


            
            