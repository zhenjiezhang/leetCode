'''
191. Number of 1 Bits
Total Accepted: 71994 Total Submissions: 190953 Difficulty: Easy

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
    	c=0
        for i in xrange(32):
        	c+=n>>i&1
        return c

print Solution().hammingWeight(11)
O