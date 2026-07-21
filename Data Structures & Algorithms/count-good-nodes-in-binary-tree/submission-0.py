# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxi):
            if not node:
                return 0
            if node.val >= maxi:
                return 1 + dfs(node.right, node.val) + dfs(node.left, node.val)
            return dfs(node.right, maxi) + dfs(node.left, maxi)
        return dfs(root, -float('inf'))