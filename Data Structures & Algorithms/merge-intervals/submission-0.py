class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals by their start time
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize the result list with the first interval
        res = [intervals[0]]

        # Step 3: Iterate over the rest of the intervals
        for start, end in intervals[1:]:
            # Get the end time of the last interval in the result list
            lastEnd = res[-1][1]

            # Step 4: Check for overlap
            if start <= lastEnd:
                # Overlapping intervals — merge them by updating the end time
                res[-1][1] = max(lastEnd, end)
            else:
                # No overlap — add the new interval to the result
                res.append([start, end])

        # Step 5: Return the merged list of intervals
        return res
