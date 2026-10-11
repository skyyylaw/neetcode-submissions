class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1
        
        while left < right:
            l = s[left].lower()
            r = s[right].lower()
            if l > 'z' or l < 'a':
                left += 1
            elif r > 'z' or r < 'a':
                right -= 1
            elif l != r:
                # print(l, r)
                return False
            elif l == r:
                left += 1
                right -= 1
        
        return True

            