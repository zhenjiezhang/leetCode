'''
296. Best Meeting Point
Total Accepted: 2214 Total Submissions: 5063 Difficulty: Hard

A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. 
The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

For example, given three people living at (0,0), (0,4), and (2,2):

1 - 0 - 0 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0

The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

Hint:

    Try to solve it in one dimension first. How can this solution apply to the two dimension case?
'''



class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        oneRows=[]
        oneCols=[]
        for i,r in enumerate(grid):
            for j,v in enumerate(r):
                if v:
                    oneRows.append(i)
                    oneCols.append(j)

        oneCols=sorted(oneCols)
        # rows are already sorted natually

        dist=0

        for r in xrange(len(oneRows)/2):
            dist+=oneRows[len(oneRows)-r-1]-oneRows[r]

        for c in xrange(len(oneCols)/2):
            dist+=oneCols[len(oneCols)-c-1]-oneCols[c]

        return dist

if __name__ == '__main__':
    print Solution().minTotalDistance([
        [0,0,0,0,1,0,1,0],
        [0,0,0,0,1,0,0,1]
        ])

        