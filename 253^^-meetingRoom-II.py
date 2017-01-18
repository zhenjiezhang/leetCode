'''
another line of interesting thinking:


Simulate event queue procession. Create event for each start and end of intervals. 
Then for start event, open one more room; for end event, close one meeting room. 
At the same time, update the most rooms that is required.

Be careful of events like [(end at 11), (start at 11)]. 
Put end before start event when they share the same happening time, so that two events can share one meeting room.






My own solution is pretty straight forward.  but the followin one is faster:
本质上，就是说每一个会的话，总会需要一个房间，所以，如果只查每个会开始时间的房的话，在开会之前结束那个会的房就不用退了。
def minMeetingRooms(self, intervals):
    ends = sorted(i.end for i in intervals)[::-1]
    rooms = 0
    for start in sorted(i.start for i in intervals):
        if start < ends[-1]:
            rooms += 1
        else:
            ends.pop()
    return rooms
'''


from heapq import heappush, heappop
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    #no need for heapq for this one
    def minMeetingRooms(self, intervals):
        timePoints=sorted([0]+[(i.start, 1) for i in intervals]+[(i.end,0) for i in intervals])
        for i in xrange(1,len(timePoints)):
            timePoints[i]=timePoints[i-1]+(1 if timePoints[i][1] else -1)
        return max(timePoints)






    def minMeetingRoomsOld(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals=sorted([[i.start, i.end] for i in intervals])
        endingTimes=[]
        maxRooms=0
        for i in xrange(len(intervals)):
            while endingTimes and endingTimes[0]<=intervals[i][0]:
                heappop(endingTimes)
            if len(endingTimes)+1>maxRooms:
                maxRooms=len(endingTimes)+1

            heappush(endingTimes, intervals[i][1])


            
        return maxRooms

if __name__ == '__main__':
    s=Solution()
    print s.minMeetingRooms([Interval(5,8),Interval(6,8)])
    print s.minMeetingRoomsOld([Interval(5,8),Interval(6,8)])


        