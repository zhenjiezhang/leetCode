'''
222. Count Complete Tree Nodes
Total Accepted: 26076 Total Submissions: 109309 Difficulty: Medium

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        leftLevels=rightLevels=1

        ll=rl=root
        while ll.left is not None:
            leftLevels+=1
            ll=ll.left
        while rl.right is not None:
            rightLevels+=1
            rl=rl.right

        if leftLevels==rightLevels:
            return 2**leftLevels-1
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)



    def countNodesTLE(self, root):
        if not root:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)


        