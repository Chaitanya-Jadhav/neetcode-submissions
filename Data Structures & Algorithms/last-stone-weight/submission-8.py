import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Step 1: Negate all values to simulate a max-heap using Python's min-heap.
        # For example, [2, 7, 4, 1, 8, 1] becomes [-2, -7, -4, -1, -8, -1].
        stones = [-s for s in stones]
        
        # Step 2: Transform the list into a heap in-place. This takes O(n) time.
        # The most negative number (the heaviest stone) will be at the root (stones[0]).
        heapq.heapify(stones)

        # Step 3: Smash stones together until there is 1 or 0 stones left.
        while len(stones) > 1:
            # Pop the smallest negative number, which represents the heaviest stone.
            first_heavist = heapq.heappop(stones) 
            
            # Pop the next smallest negative number, which is the second heaviest.
            second_heavist = heapq.heappop(stones)
            
            # Since the values are negative, 'second > first' actually means 
            # the absolute weight of 'first' is greater than 'second'.
            # (e.g., -7 > -8 is True, meaning an 8-weight stone is heavier than a 7-weight stone).
            if second_heavist > first_heavist:
                # If they are not equal, the remaining stone's weight is the difference.
                # Because they are negative, (first - second) gives us the correct negative remaining weight.
                # Example: first = -8, second = -7. (-8) - (-7) = -1. We push -1 back onto the heap.
                heapq.heappush(stones, first_heavist - second_heavist)
        
        # Step 4: Handle the edge case where all stones completely destroyed each other.
        # If the heap is empty, appending 0 prevents an IndexError on the return statement.
        stones.append(0) 
        
        # Return the absolute value to convert the negative weight back to a positive integer.
        return abs(stones[0])