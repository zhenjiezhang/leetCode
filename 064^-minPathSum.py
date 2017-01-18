'''
64. Minimum Path Sum
Total Accepted: 59673 Total Submissions: 177022 Difficulty: Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        n=len(grid)
        m=len(grid[0])
        results=[[0 for _  in xrange(m)] for _ in xrange(n)]

        results[n-1][m-1]=grid[n-1][m-1]

        if m>1:
            for i in xrange(m-2, -1, -1):
                results[n-1][i]=grid[n-1][i]+results[n-1][i+1]

        if n>1:
            for i in xrange(n-2, -1, -1):
                results[i][m-1]=grid[i][m-1]+results[i+1][m-1]

        if m>1 and n>1:
            for i in xrange(n-2, -1, -1):
                for j in xrange(m-2, -1, -1):
                    results[i][j]=grid[i][j]+min(results[i+1][j],results[i][j+1])

        return results[0][0]

if __name__=="__main__":
    solution=Solution()
    m=[[1,2,3],
    [1,2,3],
    [1,2,3]
    ]
    m1=[[1,1,1]]
    m1=[[1],[1]]
    print solution.minPathSum(m)
    print solution.minPathSum(m1)
