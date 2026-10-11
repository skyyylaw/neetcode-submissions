class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cha = None
        l = 0
        ans = 0
        for r in range(len(s)):
            if not cha:
                cha = s[r]
            else:
                if s[r] != cha:
                    if k > 0:
                        k -= 1
                    else:
                        while k == 0:
                            if s[l] != cha:
                                k += 1
                            l += 1
            ans = max(ans, r - l + 1)
        return ans