'''
258. Add Digits
Total Accepted: 66083 Total Submissions: 137598 Difficulty: Easy

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?

Hint:

    A naive implementation of the above process is trivial. Could you come up with other methods?
    What are all the possible results?
    How do they occur, periodically or randomly?
    You may find this Wikipedia article useful.
    https://en.wikipedia.org/wiki/Digital_root

    本质上，是因为每一个数在作这种运算之后，对9的余数不变。这是十进制决定的。

    '''

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
        	return  0
        res=num%9
        return res if res!=0 else 9