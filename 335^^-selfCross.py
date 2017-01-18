'''
335. Self Crossing
Total Accepted: 891 Total Submissions: 4828 Difficulty: Medium

You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:

Given x = [2, 1, 1, 2],


Return true (self crossing)

'''
from collections import deque
class Solution(object):
    def isSelfCrossing(self, x):
        if len(x)<4:
            return False
        if len(x) > 4 and x[3]==x[1] and x[2]<=x[4]+x[0]:
            return True
        for i in xrange(3,len(x)):
            if x[i]>=x[i-2] and x[i-1]<=x[i-3]:
                return True
            if i>4 and x[i-4]<=x[i-2]<=x[i]+x[i-4] and x[i-1]<=x[i-3]<=x[i-5]+x[i-1]:
                return True
        return False




    def isSelfCrossingOld(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        h=deque([[float('inf'), 0, 0] for _ in xrange(3)]) # deque with 3 element, horizontal lines with y=inf, x1=x2=0
        v=deque([[float('inf'), 0, 0] for _ in xrange(3)]) # deque with 3 element, vertical lines with x=inf, y1=y2=0

        def cross(line1, line2):
            return (line1[0]-line2[1])*(line1[0]-line2[2])<=0 and (line2[0]-line1[1])*(line2[0]-line1[2])<=0
        def touch(line1, line2):
            return line1[0]==line2[0] and max(line1[1:])>=min(line2[1:]) and max(line2[1:])>=min(line1[1:])

        pos=[0,0]
        for index,value in enumerate(x):
            oldPos=pos[:]
            if not index%2:
                pos[1]-=value if index%4 else -value
                v.popleft()
                v.append([pos[0], oldPos[1], pos[1]])
                for e in h[0], h[1]:
                    if cross(v[-1], e):
                        return True
                for e in v[0], v[1]:
                    if touch(v[-1],e):
                        return True
            else:
                pos[0]+=value if (index-1)%4 else -value
                h.popleft()
                h.append([pos[1], oldPos[0], pos[0]])
                for e in v[0],v[1]:
                    if cross(h[-1],e):
                        return True
                for e in h[0],h[1]:
                    if touch(h[-1], e):
                        return True
        return False

if __name__=='__main__':
    s=Solution()
    print s.isSelfCrossing([2,2,3,3,2,2,])

    print s.isSelfCrossing([2,2,3,1,1,])

    print s.isSelfCrossing([1,2,3,4])
    print s.isSelfCrossing([2,1,1,2])


    print s.isSelfCrossing([1,1,2,1,2])
    print s.isSelfCrossing([3,3,3,2,1,1])




        