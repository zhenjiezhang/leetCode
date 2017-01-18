'''236. Lowest Common Ancestor of a Binary Tree
Total Accepted: 31867 Total Submissions: 112204 Difficulty: Medium

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.



alternative:
in-order travers, keep the last popped node which was pushed in before the first element was found.  return the node as soon as both elements are found

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root:
        	return None

        if root==p or root==q:
        	return root

        l=self.lowestCommonAncestor(root.left,p,q)
        r=self.lowestCommonAncestor(root.right,p,q)

        if l and r:
        	return root
        else:
        	return l if l else r









        