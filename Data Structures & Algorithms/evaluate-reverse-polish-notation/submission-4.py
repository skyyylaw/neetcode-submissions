class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ('+', '-', '*', '/'):
                stack.append(int(t))
            else:
                if not stack:
                    return None
                op2 = stack.pop()
                op1 = stack.pop()
                match t:
                    case '+':
                        stack.append(op1+op2)
                    case '-':
                        stack.append(op1-op2)
                    case '*':
                        stack.append(op1*op2)
                    case '/':
                        res = op1/op2
                        if res < 0:
                            res = int(res + 1)
                        else:
                            res = int(res)
                        stack.append(res)
        return stack[0]