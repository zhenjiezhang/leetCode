# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root:
            return 0
        level=[root]
        levelNum=1

        while level:
            newLevel=[]
            for node in level:
                if not node.left and not node.right:
                    return levelNum
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            levelNum+=1
            level=newLevel
        return levelNum




    def minDepthOld(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return 1+self.minDepth(root.left)
        if root.right and not root.left:
            return 1+self.minDepth(root.right)
            
        return 1+min(self.minDepth(root.left),self.minDepth(root.right))

if __name__ == '__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)
    root.right.right=TreeNode(5)
    print Solution().minDepth(root)