# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(node):
            if not node:
                return None

            if node.val == p.val:
                return node
            if node.val == q.val:
                return node
            
            left = search(node.left)
            right = search(node.right)
            options = [node.val]
            if left:
                options.append(left.val)
            if right:
                options.append(right.val)

            if p.val in options and q.val in options:
                res = node
            else:
                res = left if left else right
            
            return res

        return search(root)