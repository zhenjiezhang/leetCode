class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    class Solution:

    def isValidBST(self, root, leftLim=-float('inf'), rightLim=float('inf')):
        return False if root and (((root.val<=leftLim or root.val>=rightLim)\
         or (root.left and (not self.isValidBST(root.left, leftLim=leftLim,rightLim=root.val)))\
         or (root.right and (not self.isValidBST(root.right, leftLim=root.val, rightLim=rightLim)))))\
          else True

if __name__ == '__main__':
	solution=Solution
	print solution.isValidBST(None)

