'''
110. Balanced Binary Tree
Total Accepted: 91426 Total Submissions: 276200 Difficulty: Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1. 
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def depth(self,node):
        if not node:
            return 0
        left, right=self.depth(node.left), self.depth(node.right)
        return 1+max(left,right) if left>=0 and right>=0 and  abs(left-right)<=1 else -1


    def isBalanced(self, root):
        return self.depth(root)>=0
        

        # if abs(self.depth(root.left)-self.depth(root.right))<=1:
        #     eturn self.isBalanced(root.left) and self.isBalanced(root.right)
if __name__ == '__main__':
    root=TreeNode(1)
    root.right=TreeNode(2)
    root.right.right=TreeNode(3)

    print Solution().isBalanced(root)