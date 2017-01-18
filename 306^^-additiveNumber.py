'''
306. Additive Number
Total Accepted: 6180 Total Submissions: 25064 Difficulty: Medium

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.

1 + 99 = 100, 99 + 100 = 199

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers? 
'''

from math import ceil

class Solution(object):
    def isAdditiveNumber(self, num):
        def valid(firstEnd, secondEnd):
            firstString, secondString=num[:firstEnd+1], num[firstEnd+1:secondEnd+1]
            while secondEnd<len(num)-1:
                thirdString=str(int(firstString)+int(secondString))
                if not num[secondEnd+1:].startswith(thirdString):
                    return False
                secondEnd+=len(thirdString)
                firstString=secondString
                secondString=thirdString
            return secondEnd==len(num)-1

        for firstEnd in xrange(len(num)/2+1):
            if num[0]=='0' and firstEnd>0:
                break
            for secondEnd in xrange(firstEnd+1, min(len(num)-firstEnd-1, firstEnd+(len(num)-1-firstEnd)/2+1)):
                if num[firstEnd+1]=='0' and secondEnd-firstEnd>1:
                    break
                if valid(firstEnd, secondEnd):
                    return True

        return False
        





    def isAdditiveNumberOld(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def valid(num, firstEnd, secondEnd):
            # print firstEnd, secondEnd, num

            thirdNum=int(num[secondEnd+1:])
            secondNum=int(num[firstEnd+1:secondEnd+1])

            if thirdNum < secondNum:
                return False

            firstString=str(thirdNum-secondNum)

            if len(firstString)>firstEnd+1 or num[firstEnd+1-len(firstString): firstEnd+1]!=firstString:
                return False
            elif len(firstString)==firstEnd+1:
                return True
            else:
                return valid(num[:secondEnd+1],firstEnd-len(firstString),firstEnd)

        n=len(num)
        for secondEnd in xrange(n-2, int(ceil(n/2.0)-2),-1):
            if int(num[secondEnd+1])==0 and n-1-secondEnd>1:
                continue

            secondEndNum=int(num[secondEnd])

            thirdEndNum=int(num[-1])
            firstEndNum=thirdEndNum-secondEndNum if thirdEndNum>=secondEndNum else \
            thirdEndNum-secondEndNum+10

            for firstEnd in xrange(secondEnd-1,secondEnd-(n-1-secondEnd)-1,-1):
                if int(num[firstEnd])==firstEndNum and (int(num[firstEnd+1]) or secondEnd-firstEnd==1) and\
                 valid(num, firstEnd, secondEnd):
                    return True
                else:
                    continue
        return False

        

if __name__ == '__main__':
    print Solution().isAdditiveNumber("0235813")
    print Solution().isAdditiveNumber('101')


    print Solution().isAdditiveNumberOld('199100199')
    print Solution().isAdditiveNumberOld('101')

