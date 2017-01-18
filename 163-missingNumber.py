'''
163. Missing Ranges
Total Accepted: 7673 Total Submissions: 27638 Difficulty: Medium

Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"]. 
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        return l*(l+1)/2-sum(nums)


        '''
        slower solution below
        '''

        l=len(nums)
        
        for i in xrange(l):

        	while nums[i]!=i and nums[i]!=l:
        		nums[nums[i]],nums[i]=nums[i],nums[nums[i]]

        index=l
        for i in xrange(l):
        	if nums[i]==n:
        		index=i
        return index

if __name__=='__main__':
	print Solution().missingNumber([3,2,0])