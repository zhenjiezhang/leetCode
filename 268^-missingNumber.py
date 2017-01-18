'''
268. Missing Number
Total Accepted: 36921 Total Submissions: 94949 Difficulty: Medium

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity? 

three methods:
'''
class Solution(object):
    def missingNumber(self, nums):
        return (len(nums)+1)*len(nums)/2-sum(nums)





    def missingNumberXor(self, nums):
        return reduce(lambda x,y:x^y, nums+range(len(nums)+1))




    def missingNumberClassic(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i,n in enumerate(nums):
            while n!=len(nums) and i!=n:
                nums[i],nums[n]=nums[n],nums[i]
                n=nums[i]
        return nums.index(len(nums)) if len(nums) in nums else len(nums)

if __name__=='__main__':
    s=Solution()
    print s.missingNumber([1,2,0,4])