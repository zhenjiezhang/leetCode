'''
334. Increasing Triplet Subsequence
Total Accepted: 2855 Total Submissions: 8595 Difficulty: Medium

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else return false. 

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false. 
'''
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<3:
            return False

        tmp=float('inf')
        smallest=nums[0]
        for i in xrange(1,len(nums)):
            if nums[i]>smallest:
                if nums[i]>tmp:
                    return True
                tmp=nums[i]
            else:
                smallest=nums[i]
        return False


if __name__=='__main__':
    s=Solution()
    print s.increasingTriplet([2,1,4,2,3])

