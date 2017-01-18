'''
308. Range Sum Query 2D - Mutable
Total Accepted: 1345 Total Submissions: 6303 Difficulty: Hard

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
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10

Note:

    The matrix is only modifiable by the update function.
    You may assume the number of calls to update and sumRegion function is distributed evenly.
    You may assume that row1 ≤ row2 and col1 ≤ col2.

    '''


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.lookupTable=[[0]*len(matrix[0]) for _ in xrange(len(matrix))] if matrix else []
        self.matrix=[[0]*len(matrix[0]) for _ in xrange(len(matrix))] if matrix else []
        self.rows=len(matrix)
        self.cols=len(matrix[0]) if matrix else 0



        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                self.update(i,j,matrix[i][j])

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        oldVal=self.matrix[row][col]
        self.matrix[row][col]=val

        rowIndexes=self.updateIndexes(row, self.rows)
        colIndexes=self.updateIndexes(col, self.cols)

        for r in rowIndexes:
            for c in colIndexes:
                self.lookupTable[r][c]+=val-oldVal


    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.squareFromOrigin(row2,col2)-(self.squareFromOrigin(row1-1, col2) if row1 else 0)\
        -(self.squareFromOrigin(row2, col1-1) if col1 else 0) + (self.squareFromOrigin(row1-1, col1-1) \
        if row1 and col1 else 0)

    def updateIndexes(self, x, limit):
        indexes=[]
        if x==0:
            return [0]

        while x<limit:
            indexes.append(x)
            x+=x&(-x)

        return indexes

    def subIndexes(self, x):
        indexes=[0]
        while x>0:
            indexes.append(x)
            x-=x&(-x)

        return indexes

    def squareFromOrigin(self, row, col):
        rowIndexes=self.subIndexes(row)
        colIndexes=self.subIndexes(col)
        sum=0
        for r in rowIndexes:
            for c in colIndexes:
                sum+=self.lookupTable[r][c]
        return sum

if __name__ == '__main__':
    matrix=[
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
    # numMatrix=NumMatrix(matrix)
    # print numMatrix.sumRegion(2,1,4,3)
    # numMatrix.update(3,2,2)
    # print numMatrix.sumRegion(2,1,4,3)

    numMatrix=NumMatrix([
        [3,0,1,4,2],
        [5,6,3,2,1],
        [1,2,0,1,5],
        [4,1,0,1,7],
        [1,0,3,0,5]
        ])
    print numMatrix.sumRegion(2,1,4,3)
    numMatrix.update(3,2,2)
    print numMatrix.sumRegion(2,1,4,3)




        

# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.update(1, 1, 10)
# numMatrix.sumRegion(1, 2, 3, 4)