class Solution:
    def isPalindrome(self, s: str) -> bool:

        left = 0
        right = len(s) - 1
        
        while left < right:
            l = s[left].lower()
            r = s[right].lower()
            if (l > 'z' and l < 'a') or (l < '0' and l > '9') :
                left += 1
            elif (r > 'z' and r < 'a') or (e < '0' and r > '9'):
                right -= 1
            elif l != r:
                # print(l, r)
                return False
            elif l == r:
                left += 1
                right -= 1
        
        return True

            