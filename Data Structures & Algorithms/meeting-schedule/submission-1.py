"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        ints_sroted = sorted(intervals, key=lambda item: item.end)

        for i in range(1, len(intervals)):

            prev = ints_sroted[i-1]
            curr = ints_sroted[i]

            if prev.end <= curr.start:
                continue
            else:
                return False
        return True