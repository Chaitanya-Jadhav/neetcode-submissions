class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort the intervals based on their start times.
        # This helps us process them in chronological order.
        intervals.sort(key = lambda x: x[0])

        # 'res' keeps track of how many intervals we need to remove.
        res = 0
        
        # 'prevEnd' tracks the end time of the last interval we decided to keep.
        # We initialize it with the end time of the very first interval.
        prevEnd = intervals[0][1]

        # Step 2: Iterate through the remaining intervals starting from the second one.
        for start, end in intervals[1:]:
            
            if start >= prevEnd:
                # Case A: No Overlap
                # The current interval starts after or exactly when the previous one ends.
                # We can keep this interval, so we just update prevEnd to its end time.
                prevEnd = end
            
            else:
                # Case B: Overlap Detected
                # The current interval starts before the previous one finishes.
                # We HAVE to remove one of them, so we increment our result counter.
                res += 1
                
                # Greedy Choice: Which one do we "remove"? 
                # We conceptually remove the one that ends later, because an interval 
                # that stretches further into the future is more likely to overlap with upcoming intervals.
                # So, we keep the minimum end time between the two overlapping intervals.
                prevEnd = min(prevEnd, end)
        
        # Return the total number of intervals we had to remove to resolve all overlaps.
        return res