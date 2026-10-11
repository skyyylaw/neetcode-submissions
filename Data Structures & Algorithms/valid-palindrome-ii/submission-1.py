class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        used = False
        while left < right:
            if s[left] != s[right]:
                if used:
                    return False
                if s[left + 1] == s[right]:
                    left += 1
                elif s[left] == s[right - 1]:
                    right -= 1
                else:
                    return False
                used = True
            else:
                left += 1
                right -= 1
        return True