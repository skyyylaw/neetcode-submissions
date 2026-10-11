class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        rows = len(heights)
        cols = len(heights[0])

        from functools import cache

        visited = set()
        @cache
        def pa(r, c):
            if (r,c) in visited:
                return False

            if r < 0 or c < 0:
                return True
            if r >= rows or c >= cols:
                return False
            reach = False

            visited.add((r,c))
            for row, col in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if (row < 0 or row >= rows or col < 0 or col >= cols) or heights[r][c] >= heights[row][col]:
                    reach = reach or pa(row, col)
            visited.remove((r,c))

            return reach
        
        visited = set()
        @cache
        def atl(r, c):
            if (r,c) in visited:
                return False

            if r < 0 or c < 0:
                return False
            if r >= rows or c >= cols:
                return True
            reach = False

            visited.add((r,c))
            for row, col in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if (row < 0 or row >= rows or col < 0 or col >= cols) or heights[r][c] >= heights[row][col]:
                    reach = reach or atl(row, col)
            visited.remove((r,c))
            
            return reach
        
        for r in range(rows):
            for c in range(cols):
                if pa(r, c) and atl(r, c):
                    ans.append([r,c])
            
        return ans
            