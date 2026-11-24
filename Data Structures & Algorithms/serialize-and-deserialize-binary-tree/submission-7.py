# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def dfs(node):
            if not node:
                return "RETURN"
            return str(node.val) + "|" + dfs(node.left) + "|" + dfs(node.right)
        return dfs(root)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        instructions = data.split("|")
        i = 0
        def reconstruct():
            nonlocal i
            op = instructions[i]
            i += 1
            if op == "RETURN":
                return None
            node = TreeNode(int(op))
            node.left = reconstruct()
            node.right = reconstruct()
            return node
        return reconstruct()


