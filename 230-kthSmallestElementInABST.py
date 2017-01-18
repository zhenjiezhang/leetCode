'''
230. Kth Smallest Element in a BST
Total Accepted: 34337 Total Submissions: 96549 Difficulty: Medium

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        p=root
        path=[]

        while p or path:
        	if p:
        		path.append(p)
	        	p=p.left
	        else:
        		p=path.pop()
        		if k==1:
        			return p.val
        		else:
        			k-=1
        			p=p.right


