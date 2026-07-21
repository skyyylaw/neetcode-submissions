class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pa = set()
        atl = set()
        

        rows = len(heights)
        cols = len(heights[0])



        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0:
                    theset = pa
                    q = deque([(r, c)])
                    while q:
                        row, col = q.popleft()
                        theset.add((row, col))
                        for nxtrow, nxtcol in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                            if  nxtrow in range(0, rows) and nxtcol in range(0, cols):
                                if (nxtrow, nxtcol) not in theset:
                                    if heights[nxtrow][nxtcol] >= heights[row][col]:
                                        q.append((nxtrow, nxtcol))
                if r == rows-1 or c == cols-1:
                    theset = atl
                    q = deque([(r, c)])
                    while q:
                        row, col = q.popleft()
                        theset.add((row, col))
                        for nxtrow, nxtcol in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                            if  nxtrow in range(0, rows) and nxtcol in range(0, cols):
                                if (nxtrow, nxtcol) not in theset:
                                    if heights[nxtrow][nxtcol] >= heights[row][col]:
                                        q.append((nxtrow, nxtcol))

               

        ans = []
        for (r, c) in pa:
            if (r,c) in atl:
                ans.append((r, c))
        
        return ans