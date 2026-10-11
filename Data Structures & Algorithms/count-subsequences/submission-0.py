class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sourceLength = len(s)
        targetLength = len(t)
        # we are desigining our 2d dp to mean:
        # dp[i][j] = number of ways we can form t[:i] using s[:j]
        dp = [ [0] * (sourceLength+1) for _ in range(targetLength+1)]
        # 
        dp[0][0] = 1


"""
    c   ca  caa caaa    caaat
c   1   1   1   1       1
ca      1   2   3       3
cat         0
    



"""