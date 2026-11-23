# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        preorderIndexLookup = {}
        inorderIndexLookUp = {}
        for i, v in enumerate(preorder):
            preorderIndexLookup[v] = i
        for i, v in enumerate(inorder):
            inorderIndexLookUp[v] = i
        
        rootIndex = 0

        def recurse(
            inLeft,
            inRight
            ):

            nonlocal rootIndex

            if inLeft > inRight:
                return None

            localRoot = preorder[rootIndex]
            rootNode = TreeNode(localRoot)
            rootIndex += 1
            
            if inLeft == inRight:
                return rootNode

            rootNode.left = recurse(inLeft, inorderIndexLookUp[localRoot]-1)
            rootNode.right = recurse(inorderIndexLookUp[localRoot]+1, inRight)

            return rootNode

        return recurse(0, len(inorder)-1)



