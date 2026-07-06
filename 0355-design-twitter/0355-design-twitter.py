class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []

        for time, tweetId in self.tweets[userId]:
            result.append((time, tweetId))

        for followee in self.following[userId]:
            for time, tweetId in self.tweets[followee]:
                result.append((time, tweetId))

        result.sort(key=lambda x: x[0], reverse=True)

        return [tweetId for _, tweetId in result[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)