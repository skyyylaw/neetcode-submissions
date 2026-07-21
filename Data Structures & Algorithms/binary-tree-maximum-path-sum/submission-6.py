# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = []
        def dfs(node):
            if not node:
                return -float('inf')
            
            left = dfs(node.left)
            mid = node.val
            right = dfs(node.right)
            
            ans.append(max(mid, mid+left, mid+right, left+mid+right))

            return max(mid, mid+left, mid+right)
        dfs(root)
        return max(ans)
