class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sourceLength = len(s)
        targetLength = len(t)
        # DP SETUP
        # we are desigining our 2d dp to mean:
        # dp[i][j] = number of ways we can form t[:i] using s[:j] 
        dp = [ [0] * (sourceLength+1) for _ in range(targetLength+1)]
        
        # DP BASECASE: we can always form t[:0] using s[:0] as they are both empty string
        for i in range(len(dp[0])):
            dp[0][i] = 1

        for i in range(1, targetLength+1):
            for j in range(1, sourceLength+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] += dp[i-1][j-1]
                dp[i][j] += dp[i][j-1]
        
        return dp[-1][-1]


"""
    ""  c   ca  caa caaa    caaat
""  1   1   1   1   1       1
c   0   1   1   1   1       1
ca  0   0   1   2   0       0
cat 0   0   0   0   0       0       
    



"""