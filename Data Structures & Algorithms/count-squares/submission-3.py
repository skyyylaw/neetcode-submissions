class CountSquares:

    def __init__(self):
        self.xNeighbors = defaultdict(list)
        self.counter = defaultdict(int)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xNeighbors[x].append(tuple(point))
        self.counter[(x, y)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x, y = point
        for anotherX, anotherY in self.xNeighbors[x]:
            if y == anotherY: 
                continue
            side = abs(y - anotherY)
            ans += self.counter[(x-side, y)] * self.counter[(x-side, anotherY)] 
            ans += self.counter[(x+side, y)] * self.counter[(x+side, anotherY)] 
        return ans
        
