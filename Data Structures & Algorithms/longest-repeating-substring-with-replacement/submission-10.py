class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = [0] * 26
        def minority(): # O(1)
            count = 0
            maxCha = ""
            for i, v in enumerate(counter):
                if v >= count:
                    maxCha = chr(ord('A')+i)
                    count = v
            return sum(counter) - count

        ans = 0

        left = 0
        for right in range(len(s)):
            counter[ord(s[right]) - ord('A')] += 1
            while minority() > k:
                counter[ord(s[left]) - ord('A')] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans