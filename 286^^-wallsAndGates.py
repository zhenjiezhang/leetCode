'''
286. Walls and Gates
Total Accepted: 5836 Total Submissions: 16208 Difficulty: Medium

You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

For example, given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''
from collections import deque

class Solution(object):
    def wallsAndGates(self, rooms):
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j]==0:
                    front=deque([[i,j,0]]) # [x,y, distance]
                    while front:
                        f=front.popleft()
                        x,y, frontDist=f
                        neighbors=[[x,y-1], [x-1, y], [x, y+1], [x+1, y]]
                        for neighbor in neighbors:
                            if neighbor[0]>=0 and neighbor[0]<len(rooms) and neighbor[1]>=0 and neighbor[1]<len(rooms[0])\
                             and rooms[neighbor[0]][neighbor[1]]>frontDist+1:
                                rooms[neighbor[0]][neighbor[1]]=frontDist+1
                                front.append(neighbor+[frontDist+1])


    def wallsAndGatesOld(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        for i in xrange(len(rooms)):
            for j in xrange(len(rooms[0])):
                if rooms[i][j]==0:
                    front=[[i,j]]
                    frontDist=0
                    while front:
                        # print front
                        newFront=[]

                        for f in front:
                            x,y=f
                            neighbors=[[x,y-1], [x-1, y], [x, y+1], [x+1, y]]
                            for neighbor in neighbors:
                                if neighbor[0]>=0 and neighbor[0]<len(rooms) and neighbor[1]>=0 and neighbor[1]<len(rooms[0])\
                                 and rooms[neighbor[0]][neighbor[1]]>frontDist+1:
                                    rooms[neighbor[0]][neighbor[1]]=frontDist+1
                                    newFront.append(neighbor)


                        front=newFront
                        # print front
                        frontDist+=1

if __name__ == '__main__':
    rooms=[
    [float('inf'), -1,  0,  float('inf')],
    [float('inf'), float('inf'), float('inf'),  -1],
    [float('inf'),  -1, float('inf'),  -1],
    [0,  -1, float('inf'), float('inf')]
    ]

    s=Solution()
    s.wallsAndGates(rooms)
    print rooms
    rooms=[
    [float('inf'), -1,  0,  float('inf')],
    [float('inf'), float('inf'), float('inf'),  -1],
    [float('inf'),  -1, float('inf'),  -1],
    [0,  -1, float('inf'), float('inf')]
    ]

    s.wallsAndGatesOld(rooms)
    print rooms



