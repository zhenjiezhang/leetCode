'''
74. Search a 2D Matrix
Total Accepted: 66556 Total Submissions: 202400 Difficulty: Medium

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

Given target = 3, return true.
'''
import bisect
class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        line=bisect.bisect([matrix[i][0] for i in xrange(len(matrix))],target)
        if line>0:
            col=bisect.bisect(matrix[line-1],target)
            if matrix[line-1][col-1]==target:
                return True
        return False

if __name__=="__main__":
    solution=Solution()
    m=[[1,2,3],
       [4,5,5],
       [7,8,9]]
    m=[[1,2,6]]
    print solution.searchMatrix(m,6)



        