class Solution:
    def checkValidString(self, s: str) -> bool:
        mostLeft = 0
        leastLeft = 0
        for c in s:
            match c:
                case '(':
                    mostLeft += 1
                    leastLeft += 1
                case '*':
                    mostLeft += 1 # used as a left
                    leastLeft -= 1 # used as a right
                case ')':
                    mostLeft -= 1
                    leastLeft -= 1
            if mostLeft < 0:
                return False
            leastLeft = max(0, leastLeft) # discard the cases where we already run out of left to match right
        return leastLeft == 0