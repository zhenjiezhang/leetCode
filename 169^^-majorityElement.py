'''
169. Majority Element
Total Accepted: 88844 Total Submissions: 225744 Difficulty: Easy

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
    	c=0
        for i in num:
        	if c==0:
        		m=i
        		c=1
        	elif i==m:
        		c+=1
        	else:
        		c-=1
        return m

