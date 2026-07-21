class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        def flood(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            
            flood(r-1, c)
            flood(r+1, c)
            flood(r, c-1)
            flood(r, c+1)
        
        ans = 0
        
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    ans += 1
                    flood(r, c)
        
        return ans