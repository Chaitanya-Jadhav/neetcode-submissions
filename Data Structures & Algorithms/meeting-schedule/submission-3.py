# Definition of Interval:
# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # STEP 1: Sort the meetings based on their start times.
        # Intuition: If meetings are in chronological order, any overlapping 
        # meetings will end up right next to each other in the list.
        intervals.sort(key = lambda x: x.start)

        # STEP 2: Iterate through the sorted list starting from the second meeting (index 1).
        for i in range(1, len(intervals)):
            prev_meeting = intervals[i-1] # The meeting we just looked at
            curr_meeting = intervals[i]   # The meeting we are currently evaluating

            # STEP 3: Check for a scheduling conflict.
            # If the current meeting starts BEFORE the previous meeting has finished, 
            # they overlap, meaning the person cannot attend both.
            if curr_meeting.start < prev_meeting.end:
                return False 

        # STEP 4: If the loop completes without finding any overlaps, 
        # the schedule is clear and the person can attend all meetings.
        return True