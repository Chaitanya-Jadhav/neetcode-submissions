import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # STEP 1: Simulate a Max-Heap
        # Python's built-in 'heapq' module only implements a Min-Heap.
        # To make it act like a Max-Heap, we invert the values by making them negative.
        # For example, [3, 2, 1, 5, 6, 4] becomes [-3, -2, -1, -5, -6, -4].
        # The largest positive number becomes the smallest negative number.
        maxHeap = [-n for n in nums] 
        
        # STEP 2: Heapify
        # This function rearranges the list in-place into a valid heap structure.
        # It takes O(N) time. After this, the smallest negative number 
        # (which represents our largest original number) will be at index 0.
        heapq.heapify(maxHeap)

        # STEP 3: Pop elements until we reach the k-th largest
        # We want the k-th largest, which means we need to discard the 
        # (k - 1) elements that are larger than it.
        while k > 1:
            # heappop removes and returns the smallest item from the heap.
            # In our inverted heap, this effectively removes the largest original number.
            heapq.heappop(maxHeap)
            k -= 1 # Decrement k to keep track of how many items we've popped
        
        # STEP 4: Return the result
        # The element currently at the root of the heap (index 0) is the k-th largest.
        # We must negate it again (-maxHeap[0]) to revert it back to its original positive value.
        return -maxHeap[0]