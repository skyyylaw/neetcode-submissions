class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges:
            return True

        graph = defaultdict(list)
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        if len(graph) != n:
            return False
        
        visited = set()
        def dfs(parent, node):
            if node in visited:
                return False
            visited.add(node)
            res = True
            for nxt in graph[node]:
                if nxt != parent:
                    res = res and dfs(node, nxt)
            return res
        
        

        return True if dfs(-1, 0) and len(visited) == n else False
            
        
        
