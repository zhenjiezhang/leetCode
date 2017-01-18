'''221. Maximal Square
Total Accepted: 22963 Total Submissions: 101629 Difficulty: Medium

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4. 
'''


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return 0

        r,c=len(matrix),len(matrix[0])


        areaMatrix=[[0 for i in xrange(c+1)] for j in xrange(r+1)]


        maxEdge=0

        for i in xrange(1,r+1):
            for j in xrange(1,c+1):
                areaMatrix[i][j]=(min(areaMatrix[i-1][j],areaMatrix[i][j-1],areaMatrix[i-1][j-1])+1) if int(matrix[i-1][j-1])==1 else 0
                if areaMatrix[i][j]>maxEdge:
                    maxEdge=areaMatrix[i][j]

        return maxEdge**2

if __name__ == '__main__':
#     print Solution().maximalSquare(['10100',
# '10111',
# '11111',
# '10010'])
    print Solution().maximalSquare(['10'])