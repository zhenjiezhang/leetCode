'''
304. Range Sum Query 2D - Immutable
Total Accepted: 7835 Total Submissions: 36294 Difficulty: Medium

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:

    You may assume that the matrix does not change.
    There are many calls to sumRegion function.
    You may assume that row1 ≤ row2 and col1 ≤ col2.

    '''
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if matrix:
            self.sumBoard=[[0 for i in xrange(len(matrix[0]))] for j in xrange(len(matrix))]
            self.sumBoard[0][0]=matrix[0][0]
            for i in xrange(1,len(matrix[0])):
                self.sumBoard[0][i]=self.sumBoard[0][i-1]+matrix[0][i]

            for i in xrange(1,len(matrix)):
                self.sumBoard[i][0]=self.sumBoard[i-1][0]+matrix[i][0]

            for i in xrange(1,len(matrix)):
                for j in xrange(1,len(matrix[0])):
                    self.sumBoard[i][j]=self.sumBoard[i-1][j]+self.sumBoard[i][j-1]\
                    -self.sumBoard[i-1][j-1]+matrix[i][j]
        else:
            self.sumBoard=[]
        # print self.sumBoard

        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int 
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumBoard[row2][col2]-(self.sumBoard[row2][col1-1] if col1>0 else 0)-\
        (self.sumBoard[row1-1][col2] if row1>0 else 0) + \
        (self.sumBoard[row1-1][col1-1] if (row1>0 and col1>0) else 0)

if __name__ == '__main__':
    matrix=[
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
    m2=[[8,-4,5,8],
        [-1,4,4,8],
        [-2,3,1,8]]
    numM=NumMatrix(m2)
    print numM.sumRegion(0,1,0,2)
        


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)