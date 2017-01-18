'''
85. Maximal Rectangle
Total Accepted: 36801 Total Submissions: 160978 Difficulty: Hard

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area. 
'''
'''
Same idea but clever in implementation:

def maximalRectangle(self, matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n + 1)
    ans = 0
    for row in matrix:
        for i in xrange(n):
            height[i] = height[i] + 1 if row[i] == '1' else 0
        stack = [-1]
        for i in xrange(n + 1):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - 1 - stack[-1]
                ans = max(ans, h * w)
            stack.append(i)
    return ans
    '''

class Solution:
    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def largestRectangleArea(self, height):
        if not height:
            return 0
        stack=[0]
        maxArea=0
        height=[0]+height+[0]

        for i in range(1, len(height)):
            while stack and height[i]<height[stack[-1]]:
                area=height[stack.pop()]*(i-stack[-1]-1)
                if area>maxArea:
                    maxArea=area
            while stack and height[i]==height[stack[-1]]:
                stack.pop()
            
            stack.append(i)

        return maxArea

    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        numMatrix=[[0]*len(matrix[0]) for _ in xrange(len(matrix))]

        for l in xrange(len(matrix)):

            i=0
            while i < len(matrix[0]):
                if matrix[l][i]=='1':
                    start=i
                    while i < len(matrix[0]) and matrix[l][i]=='1':
                        i+=1
                    for j in range(start, i):
                        numMatrix[l][j]=j-start+1
                i+=1

        maxArea=0
        for height in zip(*numMatrix):
            Area=self.largestRectangleArea(list(height))
            if Area>maxArea:
                maxArea=Area
        return maxArea




if __name__=="__main__":
    matrix=[["0","0","0","0","1","1","1","1","0","0"],\
            ["1","0","1","1","1","1","0","0","0","0"],\
            ["1","0","1","1","1","1","1","0","0","0"],\
            ["0","0","1","1","1","1","0","0","0","0"],\
            ["1","0","1","1","1","0","0","1","0","0"],\
            ["1","0","1","1","1","1","0","0","0","0"],\
            ]
    matrix1=["0"
            ]

    print Solution().maximalRectangle(matrix)
    print Solution().maximalRectangle(matrix1)




