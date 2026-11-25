class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        from functools import cache
        rows = len(matrix)
        cols = len(matrix[0])

        @cache
        def search(r, c):
            nonlocal rows, cols
            maxPath = 1
            for d in (-1, 1):
                for nr, nc in ((r+d,c), (r, c+d)):
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or matrix[nr][nc] >= matrix[r][c]:
                        continue
                    maxPath = max(maxPath, search(nr, nc) + 1)
            return maxPath
        
        output = 0
        for r in range(rows):
            for c in range(cols):
                output = max(output, search(r,c))
        
        return output
            