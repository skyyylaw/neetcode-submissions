class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        neighborsOf = defaultdict(list)
        rows = len(grid)
        cols = len(grid[0])

        freshCount = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    continue
                elif grid[r][c] == 1:
                    freshCount += 1

                key = (r, c)
                if r-1 >= 0 and grid[r-1][c] != 0:
                    neighborsOf[key].append((r-1, c))
                if r+1 < rows and grid[r+1][c] != 0:
                    neighborsOf[key].append((r+1, c))
                if c-1 >= 0 and grid[r][c-1] != 0:
                    neighborsOf[key].append((r, c-1))
                if c+1 < cols and grid[r][c+1] != 0:
                    neighborsOf[key].append((r, c+1))
        
        if freshCount == 0:
            return 0

        nextRottingFruits = []

        for k in neighborsOf:
            if grid[k[0]][k[1]] == 2:
                nextRottingFruits += neighborsOf[k]

        nextRottingFruits = deque(nextRottingFruits)
        rottedFresh = set()
        temp = []
        time = 0
        while nextRottingFruits:
            r,c = nextRottingFruits.popleft()
            
            if grid[r][c] == 1:
                rottedFresh.add((r,c))

            # this fresh fruit turns bad in this round
            grid[r][c] = 2

            # add all neighboring freshfruits for next round
            if r-1 >= 0 and grid[r-1][c] == 1:
                temp.append((r-1, c))
            if r+1 < rows and grid[r+1][c] == 1:
                temp.append((r+1, c))
            if c-1 >= 0 and grid[r][c-1] == 1:
                temp.append((r, c-1))
            if c+1 < cols and grid[r][c+1] == 1:
                temp.append((r, c+1))
            
            if not nextRottingFruits:
                time += 1
                for r, c in temp:
                    if grid[r][c] == 1:
                        nextRottingFruits.append((r,c))
                temp = []

        return time if len(rottedFresh) == freshCount else -1

                





