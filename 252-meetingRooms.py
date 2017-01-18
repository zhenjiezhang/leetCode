'''
252. Meeting Rooms
Total Accepted: 6715 Total Submissions: 16498 Difficulty: Easy

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false. 
'''
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals=sorted([[i.start,i.end] for i in intervals])

        for m1, m2 in zip(intervals, intervals[1:]):
            if m2[0]<m1[1]:
                return False
        return True

if __name__ == '__main__':
    s=Solution()
    print s.canAttendMeetings([[0, 30],[5, 10],[15, 20]])