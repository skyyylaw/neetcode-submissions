class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
            return 0
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        obstacleGrid[0][0] = -1
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    continue
                if r + 1 < rows and obstacleGrid[r+1][c] != 1:
                    obstacleGrid[r+1][c] += obstacleGrid[r][c]
                if c + 1 < cols and obstacleGrid[r][c + 1] != 1:
                    obstacleGrid[r][c+1] += obstacleGrid[r][c]
        # for r in obstacleGrid:
        #     print(r)
        return -obstacleGrid[-1][-1]
