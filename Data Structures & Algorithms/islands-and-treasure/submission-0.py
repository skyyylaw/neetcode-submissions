class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        def flood(r, c, dist):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] <= dist:
                return
            grid[r][c] = dist
            flood(r-1, c, dist+1)
            flood(r+1, c, dist+1)
            flood(r, c-1, dist+1)
            flood(r, c+1, dist+1)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    flood(r-1, c, 1)
                    flood(r+1, c, 1)
                    flood(r, c-1, 1)
                    flood(r, c+1, 1)