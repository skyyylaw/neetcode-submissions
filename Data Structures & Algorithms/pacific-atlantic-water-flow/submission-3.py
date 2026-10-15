class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def reverseFlow(r, c, ocean):
            if (r, c) in ocean:
                return
            ocean.add((r,c))
            for d in (1, -1):
                if r + d >= 0 and r + d < len(heights) and heights[r][c] <= heights[r+d][c]:
                    reverseFlow(r+d, c, ocean)
                if c + d >= 0 and c + d < len(heights[0]) and heights[r][c] <= heights[r][c+d]:
                    reverseFlow(r, c+d, ocean)
        
        pacific = set()
        atlantic = set()
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r == 0 or c == 0:
                    reverseFlow(r, c, pacific)
                if r == len(heights)-1 or c == len(heights[0])-1:
                    reverseFlow(r, c, atlantic)
        
        output = []

        for r, c in pacific:
            if (r,c) in atlantic:
                output.append([r,c])
        
        return output
