# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs_cmp(x, y):
            if (not x and y) or (x and not y) or (x and y and x.val != y.val):
                return False
            if not x and not y:
                return True
            return dfs_cmp(x.left, y.left) and dfs_cmp(x.right, y.right)
        return dfs_cmp(p, q)