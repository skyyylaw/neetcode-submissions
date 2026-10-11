class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix = defaultdict(list)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r not in prefix:
                    prefix[r].append(matrix[r][c])
                else:
                    prefix[r].append(prefix[r][-1]+matrix[r][c])
        self.pre = prefix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row2, row1-1, -1):
            res += self.pre[r][col2] - self.pre[r][col1-1]
        return res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)