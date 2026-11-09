class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        from heapq import heappush, heappop
        
        n = len(grid)
        visited = set()
        whereAmI = [(grid[0][0], 0, 0)]
        currentWaterLevel = 0
        
        while whereAmI:
            waterLevelHere, r, c = heappop(whereAmI)
            currentWaterLevel = max(currentWaterLevel, waterLevelHere)
            visited.add((r, c))

            # print(r, c)
            
            if (r, c) == (n-1, n-1):
                return currentWaterLevel
            
            for d in (1, -1):
                newR = r + d
                newC = c + d
                for newR, newC in ((newR, c), (r, newC)):
                    if newR < 0 or newR >= n:
                        continue
                    if newC < 0 or newC >= n:
                        continue
                    if (newR, newC) not in visited:
                        heappush(whereAmI, (grid[newR][newC], newR, newC))
                        visited.add((newR, newC))