class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        targetRow = None

        top = 0
        bot = rows-1
        while top <= bot:
            mid = (top + bot) // 2
            if  matrix[mid][0] <= target <= matrix[mid][-1]:
                targetRow = mid
                break
            elif target < matrix[mid][0]:
                bot = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
        
        if targetRow == None:
            return False

        l = 0
        r = cols - 1
        while l <= r:
            mid = (l + r) // 2
            if target == matrix[targetRow][mid]:
                return True
            elif target < matrix[targetRow][mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False

