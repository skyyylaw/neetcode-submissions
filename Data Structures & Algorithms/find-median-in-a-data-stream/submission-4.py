from heapq import heappush, heappop

class MedianFinder:
    
    def __init__(self):
        self.bottomMaxHeap = []
        self.topMinHeap = []

    def addNum(self, num: int) -> None:
        heappush(self.bottomMaxHeap, -num)
        if len(self.bottomMaxHeap) > len(self.topMinHeap) + 1:
            heappush(self.topMinHeap, -heappop(self.bottomMaxHeap))
        
        if self.bottomMaxHeap and self.topMinHeap and -self.bottomMaxHeap[0] > self.topMinHeap[0]:
            bottomTemp = -heappop(self.bottomMaxHeap)
            topTemp = -heappop(self.topMinHeap)
            heappush(self.bottomMaxHeap, topTemp)
            heappush(self.topMinHeap, bottomTemp)

    def findMedian(self) -> float:
        if len(self.bottomMaxHeap) > len(self.topMinHeap):
            return -self.bottomMaxHeap[0]
        return (self.topMinHeap[0] + -self.bottomMaxHeap[0]) / 2
        
        