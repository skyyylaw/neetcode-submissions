class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # top left to top right diagnoal mirror
        # left right mirror

        def tran1():
            n = len(matrix)
            for r in range(n):
                for c in range(r, n):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        def tran2():
            n = len(matrix)
            for r in range(n):
                for c in range(n//2):
                    matrix[r][c], matrix[r][-c-1] = matrix[r][-c-1], matrix[r][c]
        tran1()
        tran2()
        # for r in matrix:
        #     print(r)
