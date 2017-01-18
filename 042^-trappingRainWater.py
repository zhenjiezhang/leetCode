'''
42. Trapping Rain Water
Total Accepted: 56528 Total Submissions: 181040 Difficulty: Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
'''



'''
this is really neat!

public int trap(int[] height) {
    int secHight = 0;
    int left = 0;
    int right = height.length - 1;
    int area = 0;
    while (left < right) {
        if (height[left] < height[right]) {
            secHight = Math.max(height[left], secHight);
            area += secHight - height[left];
            left++;
        } else {
            secHight = Math.max(height[right], secHight);
            area += secHight - height[right];
            right--;
        }
    }
    return area;
}
'''


class Solution():

	def trap(self, A):
		if len(A) <2:
			return 0
		maxLeft=maxRight=0
		leftHeight=[0]*len(A)
		rightHeight=[0]*len(A)
		waterDepth=[0]*len(A)

		for i in xrange(1:len(A)):
			if A[i-1]>maxLeft:
				maxLeft=A[i-1]
			if A[-i]>maxRight:
				maxRight=A[-i]
			leftHeight[i]=maxLeft
			rightHeight[-i-1]=maxRight
		waterDepth=[max(min(leftHeight[i], rightHeight[i])-A[i],0) for i in xrange(len(A))]
		return sum(waterDepth)








	def trapOld(self, A):
		if len(A) <2:
			return 0
		left=0
		# right=0
		lHight=A[left]
		volume=0
		total=0
		start=False

		right=len(A)-1
		rHight=A[right]

		for i in range(right+1):
			if A[i]>=lHight:
				left=i
				lHight=A[left]

				if start==True:
					start=False
					total=total+volume
					volume=0

			else:
				start=True
				volume=volume+lHight-A[i]

		# print total, A[right], A[left]

		if A[right] < A[left]:
			volume=0
			start=False
			for i in range(right,left-1,-1):
				if A[i]>=rHight:
					right=i
					rHight=A[i]

					if start==True:
						start=False
						total=total+volume
						volume=0

				else:

					start=True
					volume=volume+rHight-A[i]

		return total


if __name__=="__main__":
	solution=Solution()
	print solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
	print solution.trap([0,2,0])
	print solution.trap([4,2,3])




