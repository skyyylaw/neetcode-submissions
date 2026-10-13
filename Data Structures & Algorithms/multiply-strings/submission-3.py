class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m1 = 0
        m2 = 0
        
        for i in range(1, len(num1)+1):
            m1 += (ord(num1[-i]) - ord('0')) * 10 ** (i-1)
        
        for i in range(1, len(num2)+1):
            m2 += (ord(num2[-i]) - ord('0')) * 10 ** (i-1)
        print(m1, m2)
        return str(m1 * m2)