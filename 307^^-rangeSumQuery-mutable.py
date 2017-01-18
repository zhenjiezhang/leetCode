'''
307. Range Sum Query - Mutable
Total Accepted: 6196 Total Submissions: 36914 Difficulty: Medium

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Note:

    The array is only modifiable by the update function.
    You may assume the number of calls to update and sumRange function is distributed evenly.
    '''


class NumArray(object):

    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums=[0 for _ in xrange(len(nums))]
        self.partialSum=[0 for _ in xrange(len(nums))]
        for i in xrange(len(nums)):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        old=self.nums[i]
        self.nums[i]=val

        while i < len(self.nums):
            self.partialSum[i]+=-old+val
            i+=i&(-i)

        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumBefore(j)-self.sumBefore(i-1) if i>0 else self.sumBefore(j)
        
    def sumBefore(self, i):
        result=0
        while i >0:
            result+=self.partialSum[i]
            i-=i&(-i)

        return result+self.partialSum[0]

if __name__ == '__main__':
    nArray=NumArray([1,2,3,4,5])
    print nArray.sumRange(1,4)
    nArray.update(2,8)
    print nArray.sumRange(1,4)



        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)