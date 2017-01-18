'''
172. Factorial Trailing Zeroes
Total Accepted: 48463 Total Submissions: 154135 Difficulty: Easy

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
'''
class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        i=0
        while n>=5:
        	n/=5
        	i+=n
        return i


if __name__ == '__main__':
	print Solution().trailingZeroes(5)
