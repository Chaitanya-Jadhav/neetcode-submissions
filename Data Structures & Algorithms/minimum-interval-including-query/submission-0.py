class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Sort intervals by their starting points. 
        # This allows us to iteratively process intervals as we move through the queries.
        intervals.sort()
        
        # Min-heap to keep track of the "active" intervals.
        # It will store tuples of (interval_length, right_endpoint) so that 
        # the shortest interval always bubbles up to the top (index 0).
        minHeap = []
        
        # Dictionary to cache the result of each query.
        # We need this because we process queries in sorted order, but we must 
        # return the results in the original, unsorted order.
        res = {}

        # Pointer to track our position in the sorted intervals list
        i = 0

        # Process the queries in ascending order (Sweep-line technique).
        # This ensures we only ever need to move our interval pointer 'i' forward, never backward.
        for q in sorted(queries):
            
            # Step 1: Add all intervals that START before or at the current query 'q'
            while i < len(intervals) and intervals[i][0] <= q:
                left, right = intervals[i]
                
                # Push the length of the interval and its ending point into the heap.
                # Length is calculated as (right - left + 1) to match problem constraints.
                heapq.heappush(minHeap, (right - left + 1, right))
                i += 1

            # Step 2: Remove "expired" intervals from the top of the heap.
            # If the interval at the top of the heap ends BEFORE our current query 'q',
            # it cannot cover this query (nor any future, larger queries).
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            # Step 3: Record the answer for the current query.
            # The top of the heap (minHeap[0][0]) is guaranteed to be the shortest 
            # valid interval because of how a min-heap works. 
            # If the heap is empty, no active intervals cover 'q', so we assign -1.
            res[q] = minHeap[0][0] if minHeap else -1
        
        # Finally, construct the return array by looking up the results 
        # in the exact order the queries were originally asked.
        return [res[q] for q in queries]