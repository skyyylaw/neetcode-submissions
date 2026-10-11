class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp[0] = 1 if s[0] != '0' else 0
        if n == 1:
            return dp[-1]
        dp[1] = 2 if s[:2] >= "1" and  s[:2] <= "26" else 1
        if dp[0] == 0:
            dp[1] = 0
        if n == 2:
            return dp[-1]
            
        for i in range(2, n):
            if s[i] != '0':
                dp[i] += dp[i-1]
            else:
                dp[i] = 0
            if s[i-1:i+1] >= '1' and s[i-1:i+1] <= '26':
                dp[i] += dp[i-2]
            
        return dp[-1]           