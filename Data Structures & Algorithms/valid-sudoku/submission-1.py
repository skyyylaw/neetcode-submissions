class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                d = int(board[r][c])
                if rows[r][d - 1] == True:
                    return False
                rows[r][d - 1] = True
                if cols[c][d - 1] == True:
                    return False
                cols[c][d - 1] = True
                if boxes[r // 3 * 3 + c // 3][d-1] == True:
                    return False
                boxes[r // 3 * 3 + c // 3][d-1] = True
        return True
