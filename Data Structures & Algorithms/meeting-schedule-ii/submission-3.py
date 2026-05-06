"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List["Interval"]) -> int:
        # Step 1: Separate the start times and end times into two independent lists.
        # We do this because we only care about *when* an event (a meeting starting or ending) happens, 
        # not which specific meeting it belongs to.
        start_times = [interval.start for interval in intervals]
        end_times = [interval.end for interval in intervals]

        # Step 2: Sort both lists in chronological order.
        # This allows us to process the timeline from the earliest time to the latest time.
        start_times.sort()
        end_times.sort()

        # Variables to keep track of the room counts
        rooms_in_use = 0  # Current number of active meetings
        max_rooms = 0     # The maximum number of rooms needed at any peak time

        # Two pointers to iterate through the sorted start and end times
        start_ptr = 0
        end_ptr = 0

        # Step 3: Sweep through the timeline using the start pointer.
        # We only need to loop until we've started all meetings.
        while start_ptr < len(intervals):
            
            # If the next meeting starts BEFORE the earliest currently-running meeting ends:
            # It means we have a time overlap and need an additional room.
            if start_times[start_ptr] < end_times[end_ptr]:
                rooms_in_use += 1
                start_ptr += 1  # Move to the next start time to process
                
            # Otherwise, the earliest currently-running meeting has ended BEFORE (or exactly when) 
            # the next meeting starts. 
            # This means a room just freed up, so we decrease our active room count.
            else:
                rooms_in_use -= 1
                end_ptr += 1    # Move to the next end time since this meeting is officially over
            
            # Update the maximum rooms needed so far
            max_rooms = max(max_rooms, rooms_in_use)

        return max_rooms