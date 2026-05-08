class Twitter:
    def __init__(self):
        # Used as a global timestamp. It decreases with each new tweet.
        # WHY DECREASE?: Python's heapq is a min-heap by default. By making the
        # timestamp more negative over time, the most recent tweets will have the 
        # smallest values and naturally bubble to the top of the min-heap.
        self.count = 0
        
        # Maps a userId to a list of their tweets.
        # Format: userId -> [[count (timestamp), tweetId], ...]
        self.tweetMap = defaultdict(list)  
        
        # Maps a userId to a set of userIds they follow.
        # Using a set prevents duplicate follows and allows O(1) lookups/removals.
        self.followMap = defaultdict(set)  

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet alongside the current global timestamp.
        self.tweetMap[userId].append([self.count, tweetId])
        
        # Decrement the timestamp so the NEXT tweet in the system is "more negative" (more recent)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []       # Stores the final up to 10 tweet IDs to return
        minHeap = []   # Min-heap used to efficiently merge the sorted tweet lists

        # 1. A user should always see their own tweets in their feed.
        self.followMap[userId].add(userId)
        
        # 2. Initialize the heap with the single MOST RECENT tweet from EVERY person the user follows.
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                # The latest tweet is at the very end of the user's list
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                
                # Push: [timestamp, tweetId, authorId, index_of_next_oldest_tweet]
                # We store 'followeeId' and 'index - 1' so that if this tweet gets popped, 
                # we know exactly where to go to find this specific user's NEXT most recent tweet.
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        # 3. Extract the up to 10 most recent tweets.
        while minHeap and len(res) < 10:
            # Pop the tweet with the smallest timestamp (which is the most recent due to negative counts)
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            
            # If the user whose tweet we just popped has more older tweets...
            if index >= 0:
                # ...fetch their next oldest tweet and push it into the heap.
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followee to the follower's set of connections
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Check if the connection exists before trying to remove to avoid KeyError
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)