'''
7. Reverse Integer
Total Accepted: 114980 Total Submissions: 489349 Difficulty: Easy

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.
Have you thought about this?

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
import math

class Solution:
    # @return an integer
    def reverse(self, x):
    	if x>=0:
    		result=int(str(x)[::-1])
    	else:
    		result=-int(str(-x)[::-1])
    	return result if (result < 2**31-1 and result > -2**31) else 0

if __name__=="__main__":
	solution=Solution()
	print solution.reverse(-1012)
	print solution.reverse(100)
        
