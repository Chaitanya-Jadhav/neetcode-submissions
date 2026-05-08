class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Store k, which represents the rank of the largest element we want to find.
        self.k = k
        
        # Point our minHeap variable to the input list. 
        self.minHeap = nums
        
        # Transform the list into a valid min-heap data structure in-place.
        # In a min-heap, the smallest element always bubbles up to the root (index 0).
        # Time Complexity: O(N), where N is the number of elements in 'nums'.
        heapq.heapify(self.minHeap)
        
        # THE CORE LOGIC: We only care about the 'k' largest elements.
        # By repeatedly popping the smallest elements from the heap until its size 
        # is exactly 'k', the remaining elements are guaranteed to be the 'k' largest 
        # elements we've seen so far.
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Push the new value into our min-heap.
        # Time Complexity: O(log k) because the heap size is roughly k.
        heapq.heappush(self.minHeap, val)
        
        # If adding the new value pushed our heap size beyond 'k' (meaning we now 
        # have k+1 elements), we must remove the smallest element to get back to size 'k'.
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
            
        # At this point, the heap size is strictly 'k'. 
        # Since it's a min-heap, the smallest element among these 'k' largest elements
        # sits right at the top (index 0). This is exactly our k-th largest element!
        return self.minHeap[0]