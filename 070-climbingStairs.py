'''
70. Climbing Stairs
Total Accepted: 87922 Total Submissions: 246010 Difficulty: Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
    	if n<=1:
    		return 1

    	ways=[1 for i in xrange(n+1)]
    	for i in xrange(2,n+1):
    		ways[i]=ways[i-1]+ways[i-2]
        
        

        return ways[n]

if __name__ == '__main__':
	print Solution().climbStairs(35)

