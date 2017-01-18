'''
102. Binary Tree Level Order Traversal
Total Accepted: 83934 Total Submissions: 269733 Difficulty: Easy

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]

'''
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
    	if not root:
    		return []

        buf=[root]
        nextLevel=[]
        result=[]

        while buf:
        	val=[]
        	for node in buf:
        		val.append(node.val)
        		if node.left:
        			nextLevel.append(node.left)
        		if node.right:
        			nextLevel.append(node.right)
        	result.append(val)
        	buf=nextLevel
        	nextLevel=[]
        return result
