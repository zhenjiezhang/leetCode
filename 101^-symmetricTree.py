'''
101. Symmetric Tree
Total Accepted: 89196 Total Submissions: 270947 Difficulty: Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following is not:

    1
   / \
  2   2
   \   \
   3    3

Note:
Bonus points if you could solve it both recursively and iteratively. 


'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        return self.isSymmetric2(root, root)

    def isSymmetric2(self, pl, pr):
        if pl and pr and pl.val==pr.val:
            return self.isSymmetric2(pl.left, pr.right) and self.isSymmetric2(pl.right, pr.left)
        elif not pl and not pr:
            return True
        else:
            return False




    def isSymmetricOld(self, root):
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if root.left and root.right and root.left.val==root.right.val:
            root.left.right, root.right.right=root.right.right, root.left.right
            result=self.isSymmetric(root.left) and self.isSymmetric(root.right)
            #recover the tree, may not be necessary if only want to decide symmetry
            root.left.right, root.right.right=root.right.right, root.left.right

            return result
        else:
            return False

