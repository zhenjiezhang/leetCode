'''
136. Single Number
Total Accepted: 109221 Total Submissions: 227213 Difficulty: Medium

Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 
'''

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        return reduce (lambda x,y: x^y, A)
        

if __name__ == '__main__':
	solution=Solution()
	print solution.singleNumber([1,2,3,3,2])