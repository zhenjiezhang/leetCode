'''
333. Largest BST Subtree
Total Accepted: 1027 Total Submissions: 3873 Difficulty: Medium

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:

    10
    / \
   5  15
  / \   \ 
 1   8   7

The Largest BST Subtree in this case is the highlighted one.
The return value is the subtree's size, which is 3.

Hint:

    You can recursively use algorithm similar to 98. Validate Binary Search Tree at each node of the tree, which will result in O(nlogn) time complexity.

Follow up:
Can you figure out ways to solve it with O(n) time complexity? 
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None




    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxBSTSize=0

        def recur(root):
            if not root:
                return 0, float('inf'), -float('inf') # size of this tree, leftmost value, rightmost value
            leftTree=recur(root.left)
            rightTree=recur(root.right)

            thisSize=0
            if leftTree[0]>=0 and leftTree[2]<=root.val and rightTree[0]>=0 and rightTree[1]>=root.val:
                thisSize=1+leftTree[0]+rightTree[0]
                if self.maxBSTSize<thisSize:
                    self.maxBSTSize=thisSize
                return thisSize, min(leftTree[1], root.val), max(rightTree[2], root.val)
            else:
                return -1, 0,0 # no need to compute the leftmost and rightmost values here because -1 already indicated no BST.
        recur(root)
        return self.maxBSTSize

