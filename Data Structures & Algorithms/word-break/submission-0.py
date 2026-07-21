class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0]
        for i in range(n):
            for w in wordDict:
                if i+len(w) <= n and s[i:i+len(w)] == w and (i-1 < 0 or dp[i-1] == True):
                    dp[i+len(w)-1] = True
        # print(dp)
        return dp[-1]
                    