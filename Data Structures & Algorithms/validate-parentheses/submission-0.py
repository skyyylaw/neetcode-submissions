class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if not stack:
                    return False
                match c:
                    case ')':
                        if stack[-1] != '(':
                            return False
                    case ']':
                        if stack[-1] != '[':
                            return False
                    case '}':
                        if stack[-1] != '{':
                            return False
                stack.pop()
        return stack == []