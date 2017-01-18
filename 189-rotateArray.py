'''
189. Rotate Array
Total Accepted: 58749 Total Submissions: 291293 Difficulty: Easy

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]
Hint:
Could you do it in-place with O(1) extra space? '''


class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        nums[:]=[nums[i-k%len(nums)] for i in xrange(len(nums))]

print Solution().rotate([1,2,3,4,5,6],-8)