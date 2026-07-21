class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if 1 & n >> i:
                ans = ans | (1 << (32-i-1))
        return ans
        