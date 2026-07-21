"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        memo = dict()
        visited = set()
        def traverse(curr):
            if curr in visited:
                return
            memo[curr] = Node(curr.val)
            visited.add(curr)
            for nei in curr.neighbors:
                traverse(nei)
        traverse(node)
        for curr in memo:
            for nei in curr.neighbors:
                memo[curr].neighbors.append(memo[nei])
        return memo[node]


