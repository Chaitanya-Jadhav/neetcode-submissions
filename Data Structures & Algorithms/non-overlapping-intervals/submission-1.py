class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals based on their start time
        intervals.sort(key=lambda x: x[0])

        res = 0  # Counter to track number of intervals removed
        prevEnd = intervals[0][1]  # End time of the previous (non-overlapping) interval

        # Step 2: Iterate over the rest of the intervals
        for start, end in intervals[1:]:
            if start >= prevEnd:
                # No overlap, update previous end
                prevEnd = end
            else:
                # Overlap detected: increment removal count
                res += 1
                # Keep the interval with the earlier end time to reduce future overlaps
                prevEnd = min(end, prevEnd)

        # Step 3: Return the total number of intervals removed
        return res