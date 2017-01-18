'''
41. First Missing Positive
Total Accepted: 55638 Total Submissions: 238699 Difficulty: Hard

Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space. 
'''
'''






This is faster!!!!

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in xrange(n):
            if nums[i] <= 0: nums[i] = len(nums)+1
        for i in xrange(n):
            if abs(nums[i]) <= n: nums[abs(nums[i])-1] = -abs(nums[abs(nums[i])-1])
        for i in xrange(n):
            if nums[i] > 0: return i+1
        return n+1
'''

class Solution():
	def firstMissingPositive (self, inArray):
		inLen=len(inArray)
		i=0
		# print inLen
		while (i<inLen):
			if 0<inArray[i]<=inLen:
			    value=inArray[i]
			    while 0<value<=len(inArray) and inArray[value-1]!=value:
			    	inArray[value-1], value=value, inArray[value-1]
			i=i+1
			# print inArray

		for i in range(inLen):
			if inArray[i]!=i+1:
				return i+1
		return inLen+1
				




if __name__=="__main__":
	solution=Solution()
	A=[-1,5,7,1,6,2,3,8,12,20,-4]
	A=[8]
	A=[1,2,3,4,5,6,-1]
	A=[1,1]

	print solution.firstMissingPositive(A)


