class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dq = deque()

        def flood(r, c):
            dq = deque()
            for delta in (-1, 1):
                dq.append((r+delta, c, 1))
                dq.append((r, c+delta, 1))
            while dq:
                r, c, d = dq.popleft()
                if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] <= d:
                    continue
                grid[r][c] = d
                for delta in (-1, 1):
                    dq.append((r+delta, c, d+1))
                    dq.append((r, c+delta, d+1))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    flood(r, c)
    




                