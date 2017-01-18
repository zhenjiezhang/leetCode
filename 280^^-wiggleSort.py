'''
280. Wiggle Sort
Total Accepted: 5317 Total Submissions: 11073 Difficulty: Medium

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].


'''

'''
        
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in xrange(1, len(nums)):
            if (i%2 ^ (nums[i]>nums[i-1])): #excellent use of XOR
                nums[i], nums[i-1]=nums[i-1], nums[i]
        


if __name__ == '__main__':
    nums=[3, 5, 2, 1, 6, 4]
    s=Solution()
    s.wiggleSort(nums)
    print nums


