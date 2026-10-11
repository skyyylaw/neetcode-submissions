class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)

        if not s1 and not s2 and not s3:
            return True

        if l1 + l2 < l3:
            return False
        

        dp = [[False] * (l3+1) for _ in range(l3+1)]

        if s3[0] == s1[0]:
            dp[1][0] = True
        elif s3[0] == s2[0]:
            dp[0][1] = True
        else:
            return False

        for i in range(l3):
            for j in range(l3):

                if dp[i][j]:
                    if i + j == l3:
                        return True
                    if i < l1 and s3[i+j] == s1[i]:
                        dp[i+1][j] = True
                    if j < l2 and s3[i+j] == s2[j]:
                        dp[i][j+1] = True
        # for r in dp:
        #     print(r)
        
        return False

