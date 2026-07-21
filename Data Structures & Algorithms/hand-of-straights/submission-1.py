class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counter = defaultdict(int)
        for e in hand:
            counter[e] += 1
        
        heap = []
        for v, freq in counter.items():
            heapq.heappush(heap, (v, freq))
        
        memo = []
        storage = []
        while heap:
            v, freq = heapq.heappop(heap)
            
            if memo and v != memo[-1] + 1:
                return False

            memo.append(v)

            freq -= 1
            if freq > 0:
                storage.append((v, freq))
    
            if len(memo) == groupSize:
                for each in storage:
                    heapq.heappush(heap, each)
                memo = []
                storage = []  
        if not memo and not storage: 
            return True             
        return False
        