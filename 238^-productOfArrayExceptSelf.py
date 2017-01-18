'''

238. Product of Array Except Self
Total Accepted: 32794 Total Submissions: 79943 Difficulty: Medium

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)


constant space is trivial, as the result array is nont counted as space.
just do two passes, in the second pass, directly multiply on the result array made in the first pass.
'''

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[1]
        r=[1]
        for i in xrange(1,len(nums)):
        	l.append(l[-1]*nums[i-1])
        	r.append(r[-1]*nums[-i])
        r=r[::-1]
        return [i*j for i,j in zip(l,r)]
if __name__=='__main__':
	print Solution().productExceptSelf([1,2,3,4])


        