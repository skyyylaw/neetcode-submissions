class Solution:
    def hammingWeight(self, n: int) -> int:
        return n.bit_count()
        # ans = 0
        # for i in range(n.bit_length()):
        #     if (1 << i) & n:
        #         ans += 1
        # return ans