class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        neighborsOf = defaultdict(list)
        rows = len(grid)
        cols = len(grid[0])

        nextRottingFruits = set()

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    nextRottingFruits.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        rottedFresh = 0
        temp = set()
        
        time = -1
        while nextRottingFruits:
            r,c = nextRottingFruits.pop()

            # add all neighboring freshfruits for next round and mark them as rotten
            if r-1 >= 0 and grid[r-1][c] == 1:
                temp.add((r-1, c))
                grid[r-1][c] = 2
                rottedFresh += 1
            if r+1 < rows and grid[r+1][c] == 1:
                temp.add((r+1, c))
                grid[r+1][c] = 2
                rottedFresh += 1
            if c-1 >= 0 and grid[r][c-1] == 1:
                temp.add((r, c-1))
                grid[r][c-1] = 2
                rottedFresh += 1
            if c+1 < cols and grid[r][c+1] == 1:
                temp.add((r, c+1))
                grid[r][c+1] = 2
                rottedFresh += 1
            
            if not nextRottingFruits:
                time += 1
                nextRottingFruits = temp
                temp = set()

        return time if rottedFresh == fresh else -1

                





