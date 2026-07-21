class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = defaultdict(int)
        for e in nums:
            counter[e] += 1
        for e, freq in counter.items():
            heapq.heappush(heap, (freq, e))
            if len(heap) == k + 1:
                heapq.heappop(heap)
        return [e for freq, e in heap]