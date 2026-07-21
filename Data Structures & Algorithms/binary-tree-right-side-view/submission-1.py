# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.append((root, 0))
        prev = None
        ans = []
        while q:
            node, level = q.popleft()
            if not node:
                continue
            if prev and level > prev[1]:
                ans.append(prev[0].val)
            prev = (node, level)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
        
        if prev:
            ans.append(prev[0].val)
        return ans
