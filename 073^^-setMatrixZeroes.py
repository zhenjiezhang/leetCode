'''
73. Set Matrix Zeroes
Total Accepted: 56038 Total Submissions: 171945 Difficulty: Medium

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

click to show follow up.
Follow up:

Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

'''
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        firstX=-1
        firstY=-1

        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if matrix[i][j]==0:
                    firstX=i
                    firstY=j
                    break

        if firstX==-1:
            # print matrix
            return

        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j]==0:
                    matrix[firstX][j]=0
                    matrix[i][firstY]=0

        for i in [i for i in xrange(len(matrix[firstX])) if matrix[firstX][i]==0]:
            if i==firstY:
                continue

            for j in xrange(len(matrix)):
                matrix[j][i]=0


        for i in [i for i in xrange(len(matrix)) if matrix[i][firstY]==0]:
            for j in xrange(len(matrix[i])):
                matrix[i][j]=0
        for i in xrange(len(matrix)):
            matrix[i][firstY]=0


        # print matrix
        return

if __name__=="__main__":
    solution=Solution()
    m=[[1,0,1],
       [1,1,1],
       [1,1,0]]
    m=[[0]]
    solution.setZeroes(m)











