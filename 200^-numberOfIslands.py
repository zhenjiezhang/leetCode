'''
200. Number of Islands
Total Accepted: 33490 Total Submissions: 127909 Difficulty: Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
'''


class Solution:
    # @param grid, a list of list of characters
    # @return an integer

    def explore(self, x,y):
        self.grid[x][y]='0'

        xDisplace=[-1, 1, 1, -1]
        yDisplace=[0, -1, 1, 1]
        for xD,yD in zip(xDisplace, yDisplace):
            x+=xD
            y+=yD
            if -1<x<len(self.grid) and -1<y<len(self.grid[0]) and self.grid[x][y]=='1':
                self.explore(x,y)

    def numIslands(self, grid):

        self.grid=[[c for c in line] for line in grid]
        n=0

        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if self.grid[i][j]=='1':
                    n+=1
                    self.explore(i,j)
        return n




    def exploreIsland(self, l):
    	x,y=l
        if l in self.land:
            self.land.remove(l)
    	if x>0 and (x-1,y) in self.land:
    		self.exploreIsland((x-1,y))
    	if x<len(self.grid)-1 and (x+1,y) in self.land:
    		self.exploreIsland((x+1,y))
    	if y>0 and (x,y-1) in self.land:
    		self.exploreIsland((x,y-1))
    	if y<len(self.grid[0])-1 and (x,y+1) in self.land:
    		self.exploreIsland((x,y+1))


    def numIslandsOld(self, grid):
    	self.grid=grid
    	self.land=set([(i,j) for i in xrange(len(grid)) for j in xrange(len(grid[0])) if self.grid[i][j]=='1'])

        n=0
        while self.land:
        	n+=1
        	self.exploreIsland(self.land.pop())
        return n

print Solution().numIslands(['',
'',
'',
''])
print Solution().numIslandsOld([])

print Solution().numIslandsOld([
    '11000',
    '11000',
    '00100',
    '00011'
    ])


