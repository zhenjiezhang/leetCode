'''
263. Ugly Number
Total Accepted: 40723 Total Submissions: 114207 Difficulty: Easy

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number. 
'''
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==0:
        	return False

        for n in [2,3,5]:
        	while num%n==0:
        		num/=n

        return num==1

