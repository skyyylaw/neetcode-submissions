class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # you wont understand. its too advanced
        rows = len(matrix)
        cols = len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for i in range(rows):
                        matrix[i][c] = -1 if matrix[i][c] != 0 else 0
                    for i in range(cols):
                        matrix[r][i] = -1 if matrix[r][i] != 0 else 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == -1:
                    matrix[r][c] = 0
        