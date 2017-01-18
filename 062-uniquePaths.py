'''
62. Unique Paths
Total Accepted: 73161 Total Submissions: 209946 Difficulty: Medium

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

'''
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        results=[[0 for i in xrange(m)] for j in xrange(n)]

        results[n-1]=[1 for i in xrange(m)]
        for i in xrange(n):
        	results[i][m-1]=1

        i=n-1
        while i >0:
        	i-=1
        	j=m-1
        	while j>0:
        		j-=1
        		results[i][j]=results[i+1][j]+results[i][j+1]

        return results[0][0]

solution=Solution()
print solution.uniquePaths(3,3)

