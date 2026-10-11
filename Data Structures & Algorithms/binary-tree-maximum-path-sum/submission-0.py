# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            mid = node.val
            right = dfs(node.right)

            return max(left, left + mid, mid, mid + right, right, left + mid + right)
        return dfs(root)