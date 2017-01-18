'''
326. Power of Three
Total Accepted: 20157 Total Submissions: 56802 Difficulty: Easy

Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion? 
'''
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n >0 and not 3**19%n