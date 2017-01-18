'''
198. House Robber
Total Accepted: 51660 Total Submissions: 157311 Difficulty: Easy

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''

class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
    	if len(num)==0:
    		return 0
    	if len(num)==1:
    		return num[0]

        rob=[num[0],max(num[:2])]+[0 for i in xrange(len(num)-2)]

        for i in xrange(2,len(num)):
        	rob[i]=max(rob[i-2]+num[i],rob[i-1])
        return rob[-1]

print Solution().rob([1,3,6,2])