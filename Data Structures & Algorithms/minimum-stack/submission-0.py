class MinStack:

    def __init__(self):
        self.prefixMin = []
        self.stack = []
        

    def push(self, val: int) -> None:
        self.prefixMin.append(min(val, self.prefixMin[-1] if self.prefixMin else float('inf')))
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.prefixMin.pop()
        

    def top(self) -> int:
        return int(self.stack[-1])
        

    def getMin(self) -> int:
        return int(self.prefixMin[-1])
        
