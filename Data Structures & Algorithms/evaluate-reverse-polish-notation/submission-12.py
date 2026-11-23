class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case '+':
                    val = stack.pop() + stack.pop()
                    stack.append(val)
                case '-':
                    temp = stack.pop()
                    val =  stack.pop() - temp
                    stack.append(val)
                case '*':
                    val = stack.pop() * stack.pop()
                    stack.append(val)
                case '/':
                    temp = stack.pop()
                    val = stack.pop() / temp
                    if val < 0 and val % 1 != 0:
                        val = math.floor(val)
                        val += 1
                    else:
                        val = int(val)
                    stack.append(val)
                case _:
                    stack.append(int(t))
        return stack[0]
                