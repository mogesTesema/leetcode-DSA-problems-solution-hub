import heapq
from collections import defaultdict

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)      # userId -> list of (time, tweetId)
        self.follows = defaultdict(set)      # userId -> set of followees

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        users = self.follows[userId] | {userId}   # include self
        for u in users:
            if self.tweets[u]:
                t, tid = self.tweets[u][-1]  # most recent tweet
                idx = len(self.tweets[u]) - 1
                heapq.heappush(heap, (-t, tid, u, idx))  # max-heap by time
        
        res = []
        while heap and len(res) < 10:
            t, tid, u, idx = heapq.heappop(heap)
            res.append(tid)
            if idx > 0:  # push next tweet from same user
                nt, ntid = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-nt, ntid, u, idx - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:  # prevent self-follow
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)

