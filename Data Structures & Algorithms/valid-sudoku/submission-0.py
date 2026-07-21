class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        quads = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit != "." and (0 >= int(digit) or int(digit) >= 10):
                    return False
                if digit == ".":
                    continue
                quad = (r // 3, c // 3)
                if digit in quads[quad]:
                    return False
                quads[quad].add(digit)
                if digit in rows[r]:
                    return False
                rows[r].add(digit)
                if digit in cols[c]:
                    return False
                cols[c].add(digit)
        
        return True
