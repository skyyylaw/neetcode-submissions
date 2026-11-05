# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_):
            if not node:
                return 0

            res = 0
            if max_ == None:
                res += 1
                max_ = node.val
            elif max_ <= node.val:
                res += 1
            
            res += dfs(node.left, max(max_, node.val)) + dfs(node.right, max(max_, node.val))

            return res
        return dfs(root, None)