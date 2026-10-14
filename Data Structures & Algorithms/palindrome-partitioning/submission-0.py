class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def valid(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        output = []
        partition = []

        def backtrack(l):
            if l == len(s):
                output.append(partition.copy())
            for r in range(l, len(s)):
                if valid(l, r):
                    partition.append(s[l:r+1])
                    backtrack(r + 1)
                    partition.pop()
        
        backtrack(0)
        
        return output
                    


