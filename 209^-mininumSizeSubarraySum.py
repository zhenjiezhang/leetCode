'''
209. Minimum Size Subarray Sum
Total Accepted: 29661 Total Submissions: 114770 Difficulty: Medium

Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.
More practice:

If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).

'''


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        p1=p2=0
        pSum=0


        l=len(nums)
        mlen=l+1

        while p2<l:


            while p2<l and pSum<s:
                pSum+=nums[p2]
                p2+=1

            # print p1, p2

            if pSum<s:
                return mlen if mlen<=l else 0


            while pSum>=s:
                pSum-=nums[p1]
                p1+=1

            if p2-p1+1< mlen:
                mlen=p2-p1+1
                # print mlen
        return mlen if mlen<=l else 0

if __name__ == '__main__':
    print Solution().minSubArrayLen(3,[1,1])





