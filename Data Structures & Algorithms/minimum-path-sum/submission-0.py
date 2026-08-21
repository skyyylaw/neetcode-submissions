class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                dp[r][c] = grid[r][c]
                mini = float('inf')
                if r - 1 >= 0:
                    mini = min(mini, dp[r-1][c])
                if c - 1 >= 0:
                    mini = min(mini, dp[r][c-1])
                if mini != float('inf'):
                    dp[r][c] += int(mini)
        return dp[-1][-1]