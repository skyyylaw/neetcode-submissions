class MedianFinder:

    def __init__(self):
        self.lo = [] # max heap
        self.hi = [] # min heap

    def addNum(self, num: int) -> None:
        if not self.lo and not self.hi:
            heapq.heappush(self.lo, -num)
        elif num > -self.lo[0]:
            heapq.heappush(self.hi, num)
        else:
            heapq.heappush(self.lo, -num)
        
        while len(self.lo) - len(self.hi) > 1:
            e = -heapq.heappop(self.lo)
            heapq.heappush(self.hi, e)
        while  len(self.hi) - len(self.lo) > 1:
            e = heapq.heappop(self.hi)
            heapq.heappush(self.lo, -e)
        # print(self.lo, self.hi)
        

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        elif len(self.lo) < len(self.hi):
            return self.hi[0]
        else:
            ans = 0
            ans += -self.lo[0] if self.lo else 0
            ans += self.hi[0] if self.hi else 0
            ans /= 2
            return ans
        
        