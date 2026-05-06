class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the intervals based on their start times.
        # This is crucial because it ensures that any potential overlapping 
        # intervals are adjacent to each other in the list.
        intervals.sort(key=lambda x: x[0])

        # Step 2: Initialize our result list with the first interval.
        # We need at least one interval in our list to compare against as we iterate.
        res = [intervals[0]]

        # Step 3: Iterate through the remaining intervals, unpacking them 
        # into 'start' and 'end' variables for readability.
        for start, end in intervals[1:]:
            
            # Get the end time of the most recently added/merged interval 
            # from our result list.
            lastEnd = res[-1][1]

            # Step 4: Check for overlap.
            # If the current interval's start time is less than or equal to 
            # the last merged interval's end time, they overlap.
            if start <= lastEnd:
                # Merge them: Update the end time of the last interval in 'res'.
                # We use max() because the current interval might be completely 
                # swallowed by the previous one (e.g., merging [1, 5] and [2, 4] -> [1, 5]).
                res[-1][1] = max(lastEnd, end)
            
            # Step 5: No overlap.
            else:
                # If they don't overlap, the current interval is completely separate.
                # Simply append it to our result list.
                res.append([start, end])
        
        # Step 6: Return the final merged list.
        return res