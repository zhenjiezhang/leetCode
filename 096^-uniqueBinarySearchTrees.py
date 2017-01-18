'''
96. Unique Binary Search Trees
Total Accepted: 71956 Total Submissions: 197231 Difficulty: Medium

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

   '''

class Solution:
    # @return an integer
    def numTrees(self, n):
        numList=[0 for i in xrange(n+1)]
        numList[0]=1
        for i in xrange(1,n+1):
        	for rootPos in xrange(1,i+1):
        		left=rootPos-1
        		right=i-rootPos
        		numList[i]+=numList[left]*numList[right]
        return numList[-1]


if __name__ == '__main__':
	solution=Solution()
	print solution.numTrees(3)
