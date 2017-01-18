'''
239. Sliding Window Maximum
Total Accepted: 20238 Total Submissions: 78360 Difficulty: Hard

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Therefore, return the max sliding window as [3,3,5,5,6,7].

'''
from collections import deque

class Solution(object):

    def maxSlidingWindow(self, nums, k):
        if len(nums)<2:
            return nums
        result=[]
        d=deque()
        for i in xrange(k):
            while d and nums[d[-1]]<=nums[i]:
                d.pop()
            d.append(i)

        result.append(nums[d[0]])

        for i in xrange(k,len(nums)):
            if d[0]==i-k:
                d.popleft()
            while d and nums[d[-1]]<=nums[i]:
                d.pop()
            d.append(i)
            result.append(nums[d[0]])
        return result









    def maxSlidingWindowOld(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []

        maxf=maxb=float("-inf")
        l=len(nums)

        forward=[0 for i in xrange(l)]
        backward=[0 for i in xrange(l)]

        

        for i in xrange(l):
            if i%k==0:
                maxf=float("-inf")

            if maxf<nums[i]:
                maxf=nums[i]

            if (l-i)%k==0:
                maxb=float("-inf")

            if maxb<nums[l-1-i]:
                maxb=nums[l-1-i]

            forward[i],backward[l-1-i]=maxf,maxb

        return [max(backward[i-k+1],forward[i]) for i in xrange(k-1,l)]

if __name__=='__main__':
    print Solution().maxSlidingWindow([2,3,6,5,3,7,5,3,8,9],4)
    print Solution().maxSlidingWindowOld([2,3,6,5,3,7,5,3,8,9],4)





