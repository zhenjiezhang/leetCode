'''
250. Count Univalue Subtrees
Total Accepted: 4307 Total Submissions: 12181 Difficulty: Medium

Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,

              5
             / \
            1   5
           / \   \
          5   5   5

return 4. 




'''




# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.univalueSubtree(root)[0]

    def univalueSubtree(self,root):
        if not root:
            return 0, False


        else:
            leftNum, leftSelf=self.univalueSubtree(root.left)
            rightNum, rightSelf=self.univalueSubtree(root.right)
            selfValid=(not root.left or (root.left.val==root.val and leftSelf))\
             and (not root.right or (root.right.val==root.val and rightSelf))
            return leftNum+rightNum+(1 if selfValid else 0), selfValid


if __name__ == '__main__':
    root=TreeNode(5)
    root.left=TreeNode(5)
    # root.left.left=TreeNode(5)
    # root.left.right=TreeNode(5)
    # root.right=TreeNode(5)
    # root.right.right=TreeNode(5)


    s=Solution()
    print s.countUnivalSubtrees(root)


