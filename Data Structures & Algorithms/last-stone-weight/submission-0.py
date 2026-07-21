class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-e for e in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            a, b = heapq.heappop(stones), heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, -abs(a-b))
        return -stones[0] if stones else 0