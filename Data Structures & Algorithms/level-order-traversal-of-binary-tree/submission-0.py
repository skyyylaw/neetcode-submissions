# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = deque([(root, 1)])
        while q:
            node, level = q.popleft()
            if not node:
                continue
            if len(ans) != level:
                ans.append([])
            ans[-1].append(node.val)
            q.append((node.left, level + 1))
            q.append((node.right, level + 1))
        return ans
        