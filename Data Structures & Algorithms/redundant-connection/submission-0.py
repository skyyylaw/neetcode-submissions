class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        for i in range(len(edges)-1, -1, -1):
            a, b = edges[i]
            if len(adj[a]) > 1 and len(adj[b]) > 1:
                return edges[i]
        return None