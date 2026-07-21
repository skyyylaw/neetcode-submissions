class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # diagnal mirror
        for r in range(n):
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        # left right mirror
        for c in range(n//2):
            for r in range(n):
                matrix[r][c], matrix[r][n-1-c] = matrix[r][n-1-c], matrix[r][c]

        