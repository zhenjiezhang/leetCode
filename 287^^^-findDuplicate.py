'''
287. Find the Duplicate Number
Total Accepted: 19315 Total Submissions: 51467 Difficulty: Hard

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:

    You must not modify the array (assume the array is read only).
    You must use only constant, O(1) extra space.
    Your runtime complexity should be less than O(n2).
    There is only one duplicate number in the array, but it could be repeated more than once.

    '''

#　如果是0到n填到n+1个空里，那么一个个按nums[nums[i]]摸索过去的话的话，很容易就随便loop了，loop的点就是开始检索的点，而不会loop要中间某一点。但是如果是1-n填到n个空里，那么，如果从i=0出发的话，因为0并不存于值域，
#　所以无法loop到零，那么也就无法发生loop。这种情况下，如果中间某个数有重复，那么就会发生loop到那个数。

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1=0
        p2=nums[0]

        while p1!=p2:
            p1=nums[p1]
            p2=nums[nums[p2]]

        # key step to move 1 additional step, since the initial setup is not p1=p2=2.
        p1=nums[p1]
        p2=0

        while p1!=p2:
            p1=nums[p1]
            p2=nums[p2]

        return p1

if __name__ == '__main__':
    print Solution().findDuplicate([1,2,3,4,5,6,3])





