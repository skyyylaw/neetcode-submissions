class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isValid(l, r, used):
            while l < r:
                if s[l] != s[r]:
                    if not used:
                        return isValid(l+1, r, True) or isValid(l, r-1, True)
                    return False
                l += 1
                r -= 1
            return True

        return isValid(0, len(s)-1, False)