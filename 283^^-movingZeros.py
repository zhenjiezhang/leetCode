'''
283. Move Zeroes
Total Accepted: 53758 Total Submissions: 124460 Difficulty: Easy

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.

    '''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        p1=0
        while p1<len(nums) and nums[p1]!=0:
        	p1+=1

        if p1>=len(nums)-1:
        	return

        p2=p1+1

        while p2<len(nums):
        	while nums[p2]==0 and p2<len(nums):
        		p2+=1

        	if p2==len(nums):
        		return

        	nums[p1],nums[p2]=nums[p2],nums[p1]
        	p1+=1
        	p2+=1

        return 

if __name__=='__main__':
	a=[5]
	Solution().moveZeroes(a)
	print a