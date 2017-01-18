'''
89. Gray Code
Total Accepted: 51039 Total Submissions: 146522 Difficulty: Medium

The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2

Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.
'''
import numpy as np
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n==0:
        	return [0]

        grayCodeList=self.grayCode(n-1)
        tmp=[2**(n-1) for i in xrange(2**(n-1))]        
        for i in xrange(2**(n-1)):
        	tmp[i]+=grayCodeList[-1-i]
        grayCodeList+=tmp

        return grayCodeList

    def nPgrayCode(self, n):
        if n==0:
        	return np.array([0])

        grayCodeList=self.grayCode(n-1)

        return np.concatenate([grayCodeList,np.array(grayCodeList[::-1])+2**(n-1)])
        


if __name__ == '__main__':
	solution=Solution()
	print solution.grayCode(3)
	# print solution.nPgrayCode(3)