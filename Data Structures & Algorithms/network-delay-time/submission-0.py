class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for s, t, v in times:
            adj[s].append([t, v])
        
        dist = dict()
        for i in range(1, n+1):
            dist[i] = float('inf')
        
        q = [(0, k)]
        while q:
            time, node = heapq.heappop(q)
            if time >= dist[node]:
                continue
            dist[node] = time
            for nei, time_to_nei in adj[node]:
                heapq.heappush(q, (time + time_to_nei, nei))

        if float('inf') in dist.values():
            return -1
        
        return max(dist.values())

        
        
        
        