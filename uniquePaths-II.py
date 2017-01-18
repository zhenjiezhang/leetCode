class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):

    	n=len(obstacleGrid)
    	m=len(obstacleGrid[0])


        results=[[0 for i in xrange(m)] for j in xrange(n)]

        results[n-1][m-1]=1-obstacleGrid[n-1][m-1]

        j=m-1
        while j>0:
        	j-=1
        	results[n-1][j]=0 if obstacleGrid[n-1][j]==1 else results[n-1][j+1]

        i=n-1
        while i >0:
        	i-=1
        	j=m
        	while j>0:
        		j-=1
        		results[i][j]=0 if obstacleGrid[i][j]==1 else (results[i+1][j] if i<n-1 else 0)+(results[i][j+1] if j<m-1 else 0)
        		# print i,j, results[i][j]

        return results[0][0]

solution=Solution()
m=[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
m1=[[0],[0]]
print solution.uniquePathsWithObstacles(m1)