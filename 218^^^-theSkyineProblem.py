'''
218. The Skyline Problem
Total Accepted: 13152 Total Submissions: 63081 Difficulty: Hard

A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), 
write a program to output the skyline formed by these buildings collectively (Figure B).
Buildings Skyline Contour

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. 
It is guaranteed that 0 <= Li, Ri <= INT_MAX, 0 < Hi <= INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

    The number of buildings in any input list is guaranteed to be in the range [0, 10000].
    The input list is already sorted in ascending order by the left x position Li.
    The output list must be sorted by the x position.
    There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]





Better than mine:

class Solution(object):
def getSkyline(self, buildings):
    """
    :type buildings: List[List[int]]
    :rtype: List[List[int]]
    """
    def addsky(pos, hei):
        if sky[-1][1] != hei:
            sky.append([pos, hei])

    sky = [[-1,0]]

    # possible corner positions
    position = set([b[0] for b in buildings] + [b[1] for b in buildings])

    # live buildings
    live = []

    i = 0

    for t in sorted(position):

        # add the new buildings whose left side is lefter than position t
        while i < len(buildings) and buildings[i][0] <= t:
            heappush(live, (-buildings[i][2], buildings[i][1]))
            i += 1

        # remove the past buildings whose right side is lefter than position t
        while live and live[0][1] <= t:
            heappop(live)

        # pick the highest existing building at this moment
        h = -live[0][0] if live else 0
        addsky(t, h)


https://leetcode.com/discuss/37736/108-ms-17-lines-body-explained
108 ms, 17 lines body, explained
+15 votes
3,222 views

This is a Python version of my modification of dong.wang.1694's brilliant C++ solution. It sweeps from left to right. But it doesn't only keep heights of "alive buildings" in the priority queue and it doesn't remove them as soon as their building is left behind. Instead, (height, right) pairs are kept in the priority queue and they stay in there as long as there's a larger height in there, not just until their building is left behind.

In each loop, we first check what has the smaller x-coordinate: adding the next building from the input, or removing the next building from the queue. In case of a tie, adding buildings wins, as that guarantees correctness (think about it :-). We then either add all input buildings starting at that x-coordinate or we remove all queued buildings ending at that x-coordinate or earlier (remember we keep buildings in the queue as long as they're "under the roof" of a larger actually alive building). And then, if the current maximum height in the queue differs from the last in the skyline, we add it to the skyline.

from heapq import *

class Solution:
    def getSkyline(self, LRH):
        skyline = []
        i, n = 0, len(LRH)
        liveHR = []
        while i < n or liveHR:
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                x = LRH[i][0]
                while i < n and LRH[i][0] == x:
                    heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            else:
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heappop(liveHR)
            height = len(liveHR) and -liveHR[0][0]
            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],
        return skyline



Best?
https://leetcode.com/discuss/79931/10-line-python-solution-104-ms
def getSkyline(self, buildings):
    events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
    res, hp = [[0, 0]], [(0, float("inf"))]
    for x, negH, R in events:
        while x >= hp[0][1]: 
            heapq.heappop(hp)
        if negH: 
            heapq.heappush(hp, (negH, R))
        if res[-1][1] + hp[0][0]: 
            res += [x, -hp[0][0]],
    return res[1:]

'''        


from heapq import heappush, heappop
class Solution(object):

    def getSkyline(self, buildings):
        result=[]
        currentHeights=[]
        i=0
        
        buildings=sorted([[l, -h, r] for l, r, h in buildings])

        while i < len(buildings):

            while not currentHeights or (i <len(buildings) and buildings[i][0]<=-currentHeights[0][1]):
                if not currentHeights or -buildings[i][1]>-currentHeights[0][0]:
                    result.append([buildings[i][0], -buildings[i][1]])
                heappush(currentHeights, [buildings[i][1], -buildings[i][2]])
                i+=1

            while currentHeights and (i==len(buildings) or buildings[i][0]>-currentHeights[0][1]):
                _,x=heappop(currentHeights)
                while currentHeights and currentHeights[0][1]>=x:
                    heappop(currentHeights)
                y=currentHeights[0][0] if currentHeights else 0
                result.append([-x,-y])

        return result






    def getSkylineOld(self, buildings):
        result=[]
        currentHeights=[]

        buildings=[[-b[2], b[0], b[1]] for b in buildings]
        i=0
        while i < len(buildings):
            if currentHeights and buildings[i][0]==currentHeights[0][0]:
                currentHeights[0][2]=max(currentHeights[0][2], buildings[i][2])
            elif currentHeights and buildings[i][0]>currentHeights[0][0]:

                heappush(currentHeights, buildings[i])
            else:
                heappush(currentHeights, buildings[i])
                result.append([buildings[i][1], -buildings[i][0]])
            i+=1

            while i <len(buildings) and buildings[i][1]<=currentHeights[0][2]:
                if buildings[i][0]<currentHeights[0][0]:
                    if buildings[i][1]==result[-1][0]:
                        result[-1][1]=-buildings[i][0]
                    else:
                        result.append([buildings[i][1], -buildings[i][0]])

                heappush(currentHeights, buildings[i])
                i+=1

            while currentHeights and (i==len(buildings) or buildings[i][1]>currentHeights[0][2]):
                h,_, x=heappop(currentHeights)
                while currentHeights and currentHeights[0][0]==h:
                    x=max(heappop(currentHeights)[2],x)
                while currentHeights and currentHeights[0][2]<=x:
                    heappop(currentHeights)

                y=currentHeights[0][0] if currentHeights else 0
                result.append([x,-y])

        return result








    def getSkylineOldOld(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """

        keyPoints=sorted([(buildings[i][0], i, 1) for i in xrange(len(buildings))]+\
        [(buildings[i][1], i, -1) for i in xrange(len(buildings))])

        heightHeap=[(0,-1)]
        pastBuilding=set()
        contour=[]

        for kp in keyPoints:
            if kp[2]>0:
                heappush(heightHeap, (-buildings[kp[1]][2], kp[1]))
            else:
                pastBuilding.add(kp[1])

            while heightHeap[0][1] in pastBuilding:

                heappop(heightHeap)

            if contour and kp[0]==contour[-1][0]:
                contour.pop()

            if not contour or contour[-1][1]!=-heightHeap[0][0]:
                contour.append([kp[0],-heightHeap[0][0]])

        return contour

if __name__ == '__main__':
    print Solution().getSkyline([[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]])
    print Solution().getSkylineOld([[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]])

    # print Solution().getSkylineOld([[0,2,3],[2,5,3]])








            



 