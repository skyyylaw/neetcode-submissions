class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # you wont understand. its too advanced
        rows = len(matrix)
        cols = len(matrix[0])

        rr = set()
        cc = set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rr.add(r)
                    cc.add(c)
        for r in range(rows):
            for c in range(cols):
                if r in rr or c in cc:
                    matrix[r][c] = 0
        