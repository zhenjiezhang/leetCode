'''
99. Recover Binary Search Tree
Total Accepted: 46193 Total Submissions: 180592 Difficulty: Hard

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.
Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution? 
'''


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, modify the binary tree in-place instead.
    def nextValue(self,root):

        
        # Morris traversal
    	if not root:
    		return
    	while root:
    		if not root.left:
    			yield root
    			root=root.right
    		else:
    			lChildRight=root.left
    			while lChildRight.right and lChildRight.right!=root:
    				lChildRight=lChildRight.right
    			if not lChildRight.right:
    				lChildRight.right=root
    				root=root.left
    			else:
    				lChildRight.right=None
    				yield root
    				root=root.right



    def recoverTree(self, root):
    	oddNodes=[]
    	preNode=TreeNode(-2**32+1)
    	for node in self.nextValue(root):
    		if preNode.val>node.val:
    			oddNodes.append([preNode,node])
    		preNode=node

    	if not oddNodes:
    		return
    	if len(oddNodes)==1:
    		n1,n2=oddNodes[0]
    	else:
    		n1=oddNodes[0][0]
    		n2=oddNodes[1][1]
    		
    		
    	tmp=n1.val
    	n1.val=n2.val
    	n2.val=tmp



if __name__ == '__main__':
	root=TreeNode(6)
	root.left=TreeNode(4)
	root.left.left=TreeNode(3)
	root.left.right=TreeNode(5)
	root.right=TreeNode(7)
	root.right.right=TreeNode(8)
	solution=Solution()
	solution.recoverTree(root)

	print [n.val for n in solution.nextValue(root)]



        