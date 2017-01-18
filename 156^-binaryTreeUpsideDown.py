'''
156. Binary Tree Upside Down
Total Accepted: 7665 Total Submissions: 20869 Difficulty: Medium

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.
For example:
Given a binary tree {1,2,3,4,5},

    1
   / \
  2   3
 / \
4   5

return the root of the binary tree [4,5,2,#,#,3,1].

   4
  / \
 5   2
    / \
   3   1  


'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        if not root or not root.left:
            return root

        left=root.left
        newRoot=self.upsideDownBinaryTree(left)

        left.left=root.right if root.right else None
        left.right=root
        root.left=root.right=None

        return newRoot






    def upsideDownBinaryTreeOld(self, root):
        if not root:
            return None
        leftTip=root
        leftWing=[]
        while leftTip:
            leftWing.append(leftTip)
            leftTip=leftTip.left
        newRoot=leftTip=leftWing.pop()
        while leftWing:
            leftTip.right=leftWing.pop()
            leftTip.left=leftTip.right.right if leftTip.right.right else None
            leftTip=leftTip.right
        leftTip.right=None
        leftTip.left=None
        return newRoot

if __name__ == '__main__':
    solution=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)
    print solution.upsideDownBinaryTree(root).right.left.val






        