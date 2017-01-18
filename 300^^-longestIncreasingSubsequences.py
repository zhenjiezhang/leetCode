'''
300. Longest Increasing Subsequence
Total Accepted: 16859 Total Submissions: 50708 Difficulty: Medium

Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity? 
'''


class Solution(object):
    def lengthOfLIS_NSqure(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        longestEndingAT=[1 for i in xrange(len(nums))]

        for i in xrange(len(nums)):
            for p in xrange(i-1,-1,-1):
                if nums[p]<nums[i]:
                    if longestEndingAT[p]>longestEndingAT[i]-1:
                        longestEndingAT[i]=longestEndingAT[p]+1
                    
        return max(longestEndingAT)

    # excellent!
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        import bisect

        smallestNTailValue=[nums[0]]
        for n in nums:
            if n > smallestNTailValue[-1]:
                smallestNTailValue.append(n)
            else:
                p=bisect.bisect_right(smallestNTailValue,n)
                if p==0 or smallestNTailValue[p-1]<n:
                    smallestNTailValue[p]=n
        return len(smallestNTailValue)







if __name__ == '__main__':
    print Solution().lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])