'''
276. Paint Fence
Total Accepted: 5867 Total Submissions: 19630 Difficulty: Easy

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers. 


'''
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n==0:
            return 0
        

        ways=[k,0]

        for f in xrange(n-1):
            ways[0], ways[1]=(ways[0]+ways[1])*(k-1),ways[0]

        return ways[1]+ways[0]

if __name__ == '__main__':
    print Solution().numWays(3,2)
        