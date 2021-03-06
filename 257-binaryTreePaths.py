'''
257. Binary Tree Paths
Total Accepted: 33389 Total Submissions: 124973 Difficulty: Easy

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:

["1->2->5", "1->3"]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
        	return []
        vs=str(root.val)


        lPaths=self.binaryTreePaths(root.left)
        rPaths=self.binaryTreePaths(root.right)

        return [vs+'->'+p for p in lPaths+rPaths]\
         if (lPaths or rPaths) else [vs]