class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # CASE 1: The new interval comes completely BEFORE the current interval.
            # Since the original list is sorted, no future intervals will overlap with it either. 
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # We can immediately return the result built so far, 
                # plus the rest of the remaining intervals.
                return res + intervals[i:]
            
            # CASE 2: The new interval comes completely AFTER the current interval.
            # There is no overlap, so the current interval is safe to add to our result.
            # We continue the loop to find where the new interval actually goes.
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # CASE 3: The intervals OVERLAP.
            # We don't append anything to 'res' just yet. Instead, we merge them 
            # by updating 'newInterval' to stretch from the earliest start time 
            # to the latest end time. This modified 'newInterval' will be compared 
            # against the next intervals in the loop.
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        
        # If the loop finishes entirely without triggering Case 1, it means 
        # our 'newInterval' (which may have consumed several overlapping intervals) 
        # belongs at the very end of the list.
        res.append(newInterval)

        return res