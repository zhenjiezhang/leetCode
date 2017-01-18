'''
240. Search a 2D Matrix II
Total Accepted: 26670 Total Submissions: 81477 Difficulty: Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

Given target = 5, return true.

Given target = 20, return false.
'''
import bisect
class Solution(object):

    def searchMatrix_This_Is_Wrong(self, matrix, target):
        row=bisect.bisect([r[0] for r in matrix], target)
        if row>0:
            col=bisect.bisect(matrix[row-1],target)
        return row>0 and col>0 and matrix[row-1][col-1]==target




    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
        	return False

        rs, cs=len(matrix),len(matrix[0])

        x,y=0,cs-1
        s=matrix[x][y]

        while x<rs and y>=0:
        	if matrix[x][y]==target:
        		return True
        	elif matrix[x][y]>target:
        		y-=1
        	else:
        		x+=1
        return False

if __name__=='__main__':
	m=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
	print Solution().searchMatrix(m,20)
