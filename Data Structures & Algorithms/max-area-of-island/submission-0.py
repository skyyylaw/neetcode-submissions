class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def flood(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            return 1 + flood(r-1, c) + flood(r+1, c) + flood(r, c-1) + flood(r, c+1)
        
        res = 0
        for r in range(m):
            for c in range(n):
               res = max(res, flood(r, c)) 
        return res