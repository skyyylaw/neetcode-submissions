class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        q = []
        self.k = k
        for n in nums:
            heapq.heappush(q, n)
            while len(q) > k:
                heapq.heappop(q)
        self.q = q


    def add(self, val: int) -> int:
        q = self.q
        heapq.heappush(q,val)
        while len(q) > self.k:
            heapq.heappop(q)
        return q[0]
        
