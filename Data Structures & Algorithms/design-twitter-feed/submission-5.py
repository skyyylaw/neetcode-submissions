class Twitter:

    def __init__(self):
        self.fol = defaultdict(set)
        self.post = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        heapq.heappush(self.post[userId], (-self.time, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        memo = []

        self.fol[userId].add(userId)
        
        for followee in self.fol[userId]:
            p = self.post[followee].copy()
            for i in range(10):
                if not p:
                    break
                heapq.heappush(memo, heapq.heappop(p))
                
        for _ in range(10):
            if not memo:
                break
            res.append(heapq.heappop(memo)[1])

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fol[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fol[followerId].discard(followeeId)
        
