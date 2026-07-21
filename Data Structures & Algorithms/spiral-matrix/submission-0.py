class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        
        r = 0
        c = 0
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0

        ans = []

        while len(ans) != m*n:
            print(ans)

            visited.add((r, c))
            ans.append(matrix[r][c])

            nxt_r = r + directions[d][0]
            nxt_c = c + directions[d][1]
            if nxt_r < 0 or nxt_r >= m or nxt_c < 0 or nxt_c >= n or ((nxt_r, nxt_c) in visited):
                d = (d+1) % 4
                nxt_r = r + directions[d][0]
                nxt_c = c + directions[d][1]
            
            r = nxt_r
            c = nxt_c
            
            
            
        
        return ans



            

