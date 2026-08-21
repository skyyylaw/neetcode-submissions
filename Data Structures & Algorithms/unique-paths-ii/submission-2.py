class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
            return 0
        

        obstacleGrid[0][0] = -1
        for r in range(len(obstacleGrid)):
            for c in range(len(obstacleGrid[0])):
                if obstacleGrid[r][c] == 1:
                    continue
                if r + 1 < len(obstacleGrid) and obstacleGrid[r+1][c] != 1:
                    obstacleGrid[r+1][c] += obstacleGrid[r][c]
                if c + 1 < len(obstacleGrid[0]) and obstacleGrid[r][c + 1] != 1:
                    obstacleGrid[r][c+1] += obstacleGrid[r][c]

        return -obstacleGrid[-1][-1]
