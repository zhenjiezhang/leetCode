'''219. Contains Duplicate II
Total Accepted: 43540 Total Submissions: 151351 Difficulty: Easy

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k. 
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)<=k:
            return len(nums) >  len(set(nums))

        hashSet=set(nums[:k])
        if len(hashSet) < k:
            return True

        for i in xrange(k,len(nums)):
            hashSet.add(nums[i])
            if len(hashSet)==k:
                return True
            else:
                hashSet.remove(nums[i-k])
        return False

if __name__ == '__main__':
    print Solution().containsNearbyDuplicate([2,3,4,6,7,1,4],3)