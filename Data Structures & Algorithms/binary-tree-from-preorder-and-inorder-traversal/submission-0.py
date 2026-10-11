# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)

        index = dict()
        for i, e in enumerate(inorder):
            index[e] = i
        
        root = None
        prevRoots = set()
        created = dict()

        for val in preorder:
            
            localRoot = TreeNode(val = val) if val not in created else created[val]
            
            if not root:
                root = localRoot
            
            i = index[val]
            
            if i-1 >= 0 and inorder[i-1] not in prevRoots:
                if inorder[i-1] not in created:
                    created[inorder[i-1]] = TreeNode(val = inorder[i-1])
                localRoot.left = created[inorder[i-1]]
            if i+1 < n and inorder[i+1] not in prevRoots:
                if inorder[i+1] not in created:
                    created[inorder[i+1]] = TreeNode(val = inorder[i+1])
                localRoot.right = created[inorder[i+1]]
            
            prevRoots.add(val)
        
        return root

        
            
            
            
            