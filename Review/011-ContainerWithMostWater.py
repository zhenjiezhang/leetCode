'''
11. Container With Most Water
Total Accepted: 63305 Total Submissions: 190398 Difficulty: Medium

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container. 
'''

class Solution:
    # @return an integer
    def maxArea(self, height):
        if len(height)<2:
            return 0
        left,right=0,len(height)-1
        maxWater=0

        while left<right:
            water=min(height[left],height[right])*(right-left)
            if water>maxWater:
                maxWater=water
            if height[left]<=height[right]:
                left+=1
                while left<right and height[left]<=height[left-1]:
                    left+=1
            else:
                right-=1
                while right > left and height[right]<=height[right+1] :
                    right-=1
        return maxWater

if __name__=="__main__":
    solution=Solution()
    print solution.maxArea([1,3,4,8,8])


