class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        flag = True
        ans = ""
        i = 0
        j = 0
        while True:
            if i == len(word1):
                ans += word2[j:]
                return ans
            elif j == len(word2):
                ans += word1[i:]
                return ans
            if flag:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1
            flag = not flag