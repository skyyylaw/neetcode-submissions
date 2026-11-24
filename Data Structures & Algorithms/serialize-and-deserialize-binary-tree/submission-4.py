# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def inOrder(node):
    if not node: return ""
    return inOrder(node.left) + "#" + str(node.val[0]) + "*" + str(node.val[1]) + inOrder(node.right)
def preOrder(node):
    if not node: return ""
    return "#" +  str(node.val[0]) + "*" + str(node.val[1]) + preOrder(node.left) + preOrder(node.right)

class Codec:
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        counter = defaultdict(int)
        
        def dedupe(node):
            if not node:
                return
            counter[node.val] += 1
            node.val = (node.val, counter[node.val])
            dedupe(node.left)
            dedupe(node.right)
        dedupe(root)

        res = inOrder(root) + "|" + preOrder(root)
        # print(res)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        inOrdStr, preOrdStr = data.split("|")
        inOrd = []
        preOrd = []
        for w in inOrdStr.split("#"):
            if w: 
                ele = w.split("*")
                ele[0] = int(ele[0])
                inOrd.append(tuple(ele))
        for w in preOrdStr.split("#"): 
            if w: 
                ele = w.split("*")
                ele[0] = int(ele[0])
                preOrd.append(tuple(ele))
        
        # print(inOrd, preOrd)

        inOrderIndexMap = {}
        for i, v in enumerate(inOrd):
            inOrderIndexMap[v] = i
        
        rootIndex = 0
        def reconstruct(inOrderL, inOrderR):
            nonlocal rootIndex
            if inOrderL > inOrderR:
                return None
           
            rootVal = preOrd[rootIndex]
            root = TreeNode(rootVal[0])
            
            rootIndex += 1

            root.left = reconstruct(inOrderL, inOrderIndexMap[rootVal]-1)
            root.right = reconstruct(inOrderIndexMap[rootVal]+1, inOrderR)
            return root
        
        ans = reconstruct(0, len(inOrd)-1)
        
        return ans





