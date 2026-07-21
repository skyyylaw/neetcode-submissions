class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def flood(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == 'X' or  board[r][c] == 'Q':
                return
            board[r][c] = 'Q'
            flood(r-1, c)
            flood(r+1, c)
            flood(r, c-1)
            flood(r, c+1)
        
        for r in range(rows):
            for c in range(cols):
                if r == 0 or r == rows - 1 or c == 0 or c == cols -1:
                    flood(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != 'Q':
                    board[r][c] = 'X'
                else:
                    board[r][c] = 'O'
        

