'''
215. Kth Largest Element in an Array
Total Accepted: 39731 Total Submissions: 126691 Difficulty: Medium

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.




you can use quick select to do this too
'''
import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minHeap=nums[:k]
        heapq.heapify(minHeap)

        for i in xrange(k, len(nums)):
            if nums[i]>minHeap[0]:
                heapq.heapreplace(minHeap,nums[i])

        return minHeap[0]

if __name__ == '__main__':
    a=[8,4,5,3,2,7]
    print Solution().findKthLargest(a, 3)