'''29. Divide Two Integers
Total Accepted: 56259 Total Submissions: 368242 Difficulty: Medium

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT. 

'''

import sys

class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        if divisor==0:
            return sys.maxint
        if dividend > 2147483647 or divisor < -2147483648:
            return 2147483647

        sign=-1 if (dividend >0) ^ (divisor >0) else 1

        dividend, divisor=abs(dividend), abs(divisor)

        bit,result=0,0

        leftOver=dividend
        while divisor <= leftOver:
            while divisor << bit <= leftOver:
                bit+=1
            leftOver-=divisor << bit-1
            result+= 1 << bit-1
            bit=0

        return min(result,2147483647) if sign==1 else max(-result,-2147483648)


if __name__=="__main__":
    solution=Solution()
    print solution.divide(4,3)
    print solution.divide(100,3)
    print solution.divide(9,3)
    print solution.divide(9,-3)
    print solution.divide(100,0)
    print solution.divide(0,9)
    print solution.divide(-2147483648,1)



