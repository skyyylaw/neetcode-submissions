class Twitter:

    def __init__(self):
        self.fol = defaultdict(set)
        self.post = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.post[userId], -tweetId)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        memo = []

        self.fol[userId].add(userId)
        
        for followee in self.fol[userId]:
            p = self.post[followee].copy()
            for i in range(1, 11):
                if not p:
                    break
                heapq.heappush(memo, heapq.heappop(p))
                
        for _ in range(min(len(memo),10)):
            res.append(- heapq.heappop(memo))

        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.fol[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fol[followerId].discard(followeeId)
        
