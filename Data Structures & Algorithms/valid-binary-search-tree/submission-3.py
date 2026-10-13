# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        memo = []
        ans = set()
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            if memo and node.val <= memo[-1]:
                ans.add(False)
            memo.append(node.val)
            traverse(node.right)
        traverse(root)
        return not (False in ans)