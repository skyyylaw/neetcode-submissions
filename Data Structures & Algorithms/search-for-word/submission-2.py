class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        visited = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r<0 or r>=rows or c <0 or c>= cols or board[r][c] != word[i]:
                return False
            visited.add((r,c))
            res = False
            for rr, cc in ((r+1, c), (r-1, c), (r, c+1),(r, c-1)):
                if (rr,cc) not in visited:
                    res = res or dfs(rr, cc, i+1)
            visited.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


