# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(curr, parent, left):
            if not curr:
                return True
            if parent:
                if left and curr.val >= parent.val:
                    return False
                if not left and curr.val <= parent.val:
                    return False
            return check(curr.left, curr, True) and check(curr.right, curr, False)
        return check(root, None, False)