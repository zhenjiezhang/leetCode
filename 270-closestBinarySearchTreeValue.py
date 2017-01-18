'''
270. Closest Binary Search Tree Value
Total Accepted: 8103 Total Submissions: 24619 Difficulty: Easy

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        left=-float('inf')
        right=float('inf')
        while root:
            if target >= root.val:
                left=root.val
                root=root.right
            else:
                right=root.val
                root=root.left
        return left if target-left<=right-target else right

