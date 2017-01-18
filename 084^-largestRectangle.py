'''
84. Largest Rectangle in Histogram
Total Accepted: 52264 Total Submissions: 222634 Difficulty: Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10. 
'''

'''
Simpler but a bit of imperfect

def largestRectangleArea(self, height):
    height.append(0)
    stack = [-1]
    ans = 0
    for i in xrange(len(height)):
        while height[i] < height[stack[-1]]:
            h = height[stack.pop()]
            w = i - stack[-1] - 1
            ans = max(ans, h * w)
        stack.append(i)
    height.pop()
    return ans

'''


class Solution:
    # @param height, a list of integer
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


if __name__=="__main__":
    solution=Solution()
    print solution.largestRectangleArea([2,1,5,6,6,2,3])
    print solution.largestRectangleArea([1])
    print solution.largestRectangleArea([0,1,0,1])






