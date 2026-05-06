"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)

        for i in range(1, len(intervals)):
            meeting_prev = intervals[i-1]
            meeting_next = intervals[i]

            if meeting_next.start < meeting_prev.end:
                return False
        return True 