'''
59. Spiral Matrix II
Total Accepted: 44716 Total Submissions: 133290 Difficulty: Medium

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,
You should return the following matrix:

[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

'''
class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix=[[0 for i in xrange(n)] for j in xrange(n)]


        first=1
        for i in xrange((n+1)/2):
        	matrix[i][i:n-i]=xrange(first,first+n-2*i)
        	first+=n-2*i


        	for j in xrange(i+1,n-i):
        		matrix[j][n-i-1]=first+j-i-1
        	first+=n-2*i-1



        	matrix[n-i-1][i:n-1-i]=xrange(first+(n-2*i-2),first-1,-1)
        	first+=(n-2*i-1)


        	for j in xrange(n-i-2,i,-1):
        		matrix[j][i]=first+n-i-2-j
        	first+=n-2*i-2

       	return matrix


if __name__=="__main__":
	solution=Solution()
	print solution.generateMatrix(1)
	print solution.generateMatrix(2)
	print solution.generateMatrix(3)
	print solution.generateMatrix(4)
	print solution.generateMatrix(5)



