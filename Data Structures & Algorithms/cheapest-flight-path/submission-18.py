class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from heapq import heappush, heappop
        
        minHeap = [(0, 0, src)]
        graph = defaultdict(list)
        price = {}
        for origin, destination, p in flights:
            price[(origin, destination)] = p
            graph[origin].append(destination)
        
        cheapest = float('inf')

        dp = {}
        
        while minHeap:
            totalCost, totalFlightsUsed, airport= heappop(minHeap)
            if (totalFlightsUsed, airport) in dp:
                continue

            dp[(totalFlightsUsed, airport)] = totalCost

            nextTotalFlightsUsed = totalFlightsUsed + 1
            for nextAirport in graph[airport]:
                nextTotalCost = totalCost +  price[(airport, nextAirport)]
                if nextAirport == dst:
                    cheapest = min(cheapest, nextTotalCost)
                    continue
                elif nextTotalFlightsUsed > k:
                    continue
                heappush(minHeap,(
                    nextTotalCost, 
                    nextTotalFlightsUsed, 
                    nextAirport
                ))
            
        
        return int(cheapest) if cheapest != float('inf') else -1
            