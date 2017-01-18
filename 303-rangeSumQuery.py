class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        if nums:
            self.sumTalbe=[nums[0]]
            for n in nums[1:]:
                self.sumTalbe.append(self.sumTalbe[-1]+n)
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumTalbe[j]-(self.sumTalbe[i-1]if i >0 else 0)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)