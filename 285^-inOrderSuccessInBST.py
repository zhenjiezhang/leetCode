'''
285. Inorder Successor in BST
Total Accepted: 5515 Total Submissions: 15783 Difficulty: Medium

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null. 


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if p.right:
            p=p.right
            while p.left:
                p=p.left
            return p
        else:
            suc=None
            while root!=p:
                if p.val < root.val:
                    suc=root
                    root=root.left
                else:
                    root=root.right

            return suc