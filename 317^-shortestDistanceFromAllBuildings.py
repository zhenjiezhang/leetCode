'''
317. Shortest Distance from All Buildings
Total Accepted: 2166 Total Submissions: 7187 Difficulty: Hard

You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

    Each 0 marks an empty land which you can pass by freely.
    Each 1 marks a building which you cannot pass through.
    Each 2 marks an obstacle which you cannot pass through.

For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.
'''

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        houses=[]
        n,m=len(grid), len(grid[0])
        houses=[(i,j) for i in xrange(n) for j in xrange(m) if grid[i][j]==1]

        housesDone=0
        reachedBy=[[0]*m for _ in xrange(n)]
        totalDist=[[0]*m for _ in xrange(n)]

        currentHouseDist=[[-1]*m for _ in xrange(n)]

        for house in houses:
            currentHouseDist[house[0]][house[1]]=0
            reachFront=[house]

            newReach=False

            while reachFront:
                newFront=[]
                for land in reachFront:
                    nextLands=[(land[0]-1, land[1]),(land[0]+1, land[1]),(land[0], land[1]-1),(land[0], land[1]+1)]
                    for nextLand in nextLands:
                        x,y=nextLand
                        if x<n and x>=0 and y>=0 and y<m and grid[x][y]==0 and currentHouseDist[x][y]==-1 \
                        and reachedBy[x][y]==housesDone:
                            newReach=True
                            currentHouseDist[x][y]=currentHouseDist[land[0]][land[1]]+1
                            totalDist[x][y]+=currentHouseDist[x][y]
                            reachedBy[x][y]+=1
                            newFront.append((x,y))

                reachFront=newFront
            if not newReach:
                return -1

            housesDone+=1
            currentHouseDist=[[-1]*m for _ in xrange(n)]

        minDist=float('inf')
        for i in xrange(len(totalDist)):
            for j in xrange(len(totalDist[0])):
                if grid[i][j]==0 and reachedBy[i][j]==len(houses) and totalDist[i][j]<minDist:
                    minDist=totalDist[i][j]


        return minDist if minDist<float('inf') else -1

if __name__ == '__main__':
    solution=Solution()
    print solution.shortestDistance([
        [1,1,1,1,1,0],
        [0,0,0,0,0,1],
        [0,1,1,0,0,1],
        [1,0,0,1,0,1],
        [1,0,1,0,0,1],
        [1,0,0,0,0,1],
        [0,1,1,1,1,0]

        ])







