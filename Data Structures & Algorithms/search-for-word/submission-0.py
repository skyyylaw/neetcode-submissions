class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        from functools import cache
        visited = set()
        @cache
        def dfs(r, c, i):
            if i == len(word):
                return True
            if r<0 or r>=rows or c <0 or c>= cols or board[r][c] != word[i]:
                return False
            visited.add((r,c))
            for r, c in ((r+1, c), (r-1, c), (r, c+1),(r, c-1)):
                if (r,c) not in visited:
                    return dfs(r, c, i+1)
            visited.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


