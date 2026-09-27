class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        flag = True
        ans = []
        i = 0
        j = 0
        while True:
            if i == len(word1):
                ans.append(word2[j:])
                return "".join(ans)
            elif j == len(word2):
                ans.append(word1[i:])
                return "".join(ans)
            if flag:
                ans.append(word1[i])
                i += 1
            else:
                ans.append(word2[j])
                j += 1
            flag = not flag