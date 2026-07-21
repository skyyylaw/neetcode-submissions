# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def equal(a, b):
            if not a and not b:
                return True
            if a and b and a.val == b.val:
                return equal(a.left, b.left) and equal(a.right, b.right)
            return False
        
        def sub(node):
            if not node:
                return False
            if node.val == subRoot.val:
                a = node
                b = subRoot
                if equal(a, b):
                    return True
            ans = sub(node.left) or sub(node.right)
            return ans
        
        return sub(root)
