''''233. Number of Digit One
Total Accepted: 15413 Total Submissions: 65296 Difficulty: Medium

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.

Hint:

    Beware of overflow.



'''


class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
        	return 0

        if n<10:
        	return 1

        highN=n
        place=0

        while highN!=0:
        	place+=1
        	highN/=10

        base=10**(place-1)
        
        highN=n/base

        return (base if highN>1 else n%(base)+1)\
        +highN*(place-1)*base/10\
        +self.countDigitOne(n%(base))

if __name__=="__main__":
	print Solution().countDigitOne(114)

        