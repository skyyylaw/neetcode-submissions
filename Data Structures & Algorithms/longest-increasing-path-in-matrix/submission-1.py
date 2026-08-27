class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        memo = {}

        def dfs(r, c):
            if (r,c) in memo:
                return memo[(r,c)]
            longestPath = 1
            for rd, cd in ((1,0), (-1,0), (0, 1), (0, -1)):
                nr, nc  = r + rd, c + cd
                if 0 <= nr < rows and 0 <= nc < cols and matrix[r][c] > matrix[nr][nc]:
                    longestPath = max(longestPath, dfs(nr, nc) + 1)
            
            memo[(r, c)] = longestPath
            return memo[(r, c)]
        
        return max(dfs(r,c) for r in range(rows) for c in range(cols))
