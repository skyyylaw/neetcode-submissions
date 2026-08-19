class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        

        if l1 + l2 != l3 or (not s1 and (s2 != s3)) or (not s2 and (s1 != s3)):
            return False

        if (not s1 and (s2 == s3)) or (not s2 and (s1 == s3)):
            return True
        

        dp = [[False] * (l2+1) for _ in range(l1+1)]
        dp[0][0] = True

        for i in range(l1+1):
            for j in range(l2+1):
                if dp[i][j]:                    
                    # this means that we were able to use the first
                    # i characters from s1 and j characters from s2 
                    # to build first i + j characters of s3
                    if i < l1 and s3[i+j] == s1[i]:
                        dp[i+1][j] = True
                    if j < l2 and s3[i+j] == s2[j]:
                        if j + 1 < l2+1:
                            dp[i][j+1] = True
        
        # for r in dp:
        #     print(r)
        
        return dp[-1][-1]

