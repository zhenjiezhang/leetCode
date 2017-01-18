'''
329. Longest Increasing Path in a Matrix
Total Accepted: 4643 Total Submissions: 15689 Difficulty: Medium

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

nums = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]

Return 4
The longest increasing path is [1, 2, 6, 9].

Example 2:

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]

Return 4
The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.


Strategy is good, with some fine tuning should get the top speed.  right now faster than >70%

'''
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.matrix=matrix
        self.startFromHereLength=[[0]*len(matrix[0]) for _ in xrange(len(matrix))]
        self.maxLength=0


        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                self.explore(i,j)

        return self.maxLength

    def explore(self, i, j):
        curValue=self.matrix[i][j]
        curLength=self.startFromHereLength[i][j]
        if curLength>0:
            return

        if i>0 and self.matrix[i-1][j]>curValue:
            self.explore(i-1,j)
            curLength=max(curLength, self.startFromHereLength[i-1][j])
        if i<len(self.matrix)-1 and self.matrix[i+1][j]>curValue:
            self.explore(i+1, j)
            curLength=max(curLength, self.startFromHereLength[i+1][j])
        if j>0 and self.matrix[i][j-1]>curValue:
            self.explore(i,j-1)
            curLength=max(curLength, self.startFromHereLength[i][j-1])
        if j<len(self.matrix[0])-1 and self.matrix[i][j+1]> curValue:
            self.explore(i,j+1)
            curLength=max(curLength, self.startFromHereLength[i][j+1])

        self.startFromHereLength[i][j]=curLength+1
        if self.maxLength<self.startFromHereLength[i][j]:
           self.maxLength=self.startFromHereLength[i][j]

if __name__=="__main__":
    s=Solution()
    m=[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
    m1=[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
    print s.longestIncreasingPath(m1)








