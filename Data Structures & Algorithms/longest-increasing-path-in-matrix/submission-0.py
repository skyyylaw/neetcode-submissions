class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[-1] * cols for _ in range(rows)]

        ans = 0
        
        for r in range(rows):
            for c in range(cols):
                thisEle = matrix[r][c]
                if ((r-1 < 0 or thisEle <= matrix[r-1][c]) and
                    (c-1 < 0 or thisEle <= matrix[r][c-1]) and
                    (r+1 >= rows or thisEle <= matrix[r+1][c]) and
                    (c+1 >= cols or thisEle <= matrix[r][c+1])):
                    # this is a local min
                    dp[r][c] = 1
                    
                    # conduct bfs
                    bfs_queue = deque([(r,c)])
                    while bfs_queue:
                        rr, cc = bfs_queue.popleft()
                        ans = max(ans, dp[rr][cc])
                        if (rr-1 >= 0 and 
                            matrix[rr-1][cc] > matrix[rr][cc] and 
                            dp[rr-1][cc] < dp[rr][cc] + 1):
                                dp[rr-1][cc] = dp[rr][cc] + 1
                                bfs_queue.append((rr-1, cc))
                        if (rr+1 < rows and 
                            matrix[rr+1][cc] > matrix[rr][cc] and
                            dp[rr+1][cc] < dp[rr][cc] + 1):
                                dp[rr+1][cc] = dp[rr][cc] + 1
                                bfs_queue.append((rr+1, cc))
                        if (cc-1 >= 0 and 
                            matrix[rr][cc-1] > matrix[rr][cc] and
                            dp[rr][cc-1] < dp[rr][cc] + 1):
                                dp[rr][cc-1] = dp[rr][cc] + 1
                                bfs_queue.append((rr, cc-1))
                        if (cc+1 < cols and 
                            matrix[rr][cc+1] > matrix[rr][cc] and
                            dp[rr][cc+1] < dp[rr][cc] + 1):
                                dp[rr][cc+1] = dp[rr][cc] + 1
                                bfs_queue.append((rr, cc+1))
        
        # for r in dp:
        #     print(r)
        
        return ans
                




