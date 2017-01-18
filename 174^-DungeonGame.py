'''
174. Dungeon Game
Total Accepted: 20677 Total Submissions: 103489 Difficulty: Hard

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
-2 (K)  -3  3
-5  -10   1
10  30  -5 (P)

Notes:

    The knight's health has no upper bound.
    Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

    '''
class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        height, width=len(dungeon), len(dungeon[0])
        points=[[0]*width for _ in xrange(height)]

        point=0
        for row in xrange(height-1,-1,-1):
           point=max(1-dungeon[row][width-1],point-dungeon[row][width-1],1)
           points[row][width-1]=point
        point=0
        for col in xrange(width-1,-1,-1):
           point=max(1-dungeon[height-1][col],point-dungeon[height-1][col],1)
           points[height-1][col]=point


        for i in xrange(height-2,-1,-1):
           for j in xrange(width-2,-1,-1):
              points[i][j]=max(1-dungeon[i][j], min(points[i+1][j],points[i][j+1])-dungeon[i][j], 1)


        return points[0][0]

if __name__=="__main__":
   solution=Solution()
   dungeon=[
          [-2,-3,3],
          [-5,-10,1],
          [10,30,-5]
         ]
   dungeon=[[0,0]]
   print solution.calculateMinimumHP(dungeon)




