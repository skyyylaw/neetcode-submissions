# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def search(node, target, path):
            if not node:
                return
            path.append(node)
            if node.val == target.val:
                return 
            if target.val > node.val:
                search(node.right, target, path)
            else:
                search(node.left, target, path)
        
        pathP = []
        pathQ = []

        search(root, p, pathP)
        search(root, q, pathQ)

        for i in range(1, min(len(pathP), len(pathQ))):
            if pathQ[i] != pathP[i]:
                return pathQ[i-1]
        return pathQ[-1] if len(pathQ) < len(pathP) else pathP[-1]
                
            