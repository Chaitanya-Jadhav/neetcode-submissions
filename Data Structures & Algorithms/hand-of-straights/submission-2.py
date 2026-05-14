class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 1. Base Case Check
        # If the total number of cards cannot be evenly divided by the group size, 
        # it's impossible to form the groups.
        if len(hand) % groupSize:
            return False
        
        # 2. Count Frequencies
        # Create a hash map to keep track of how many of each card we have.
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)
        
        # 3. Initialize a Min-Heap
        # We put all unique card values into a min-heap. 
        # This allows us to always efficiently grab the smallest available card.
        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        # 4. Form Groups
        while minHeap:
            # The next group MUST start with the smallest available card.
            first = minHeap[0]

            # Try to build a sequence of length 'groupSize' starting from 'first'
            for i in range(first, first + groupSize):
                
                # If a required card is not in our count (or count reached 0 previously), 
                # we can't complete the consecutive sequence.
                if i not in count:
                    return False
                
                # 'Use' one instance of the current card
                count[i] -= 1

                # If we have completely run out of this specific card...
                if count[i] == 0:
                    # CRITICAL LOGIC: 
                    # Whenever a card's count reaches 0, it should be the current minimum card 
                    # (the root of our heap). If a larger card runs out BEFORE the smallest 
                    # available card runs out, it means we have remaining small cards but a gap 
                    # in the sequence ahead. Thus, a straight is impossible.
                    if i != minHeap[0]:
                        return False
                    
                    # Since it is the minimum card, safely remove it from the heap
                    heapq.heappop(minHeap)
                    
        # If we successfully grouped all cards without returning False, we did it!
        return True