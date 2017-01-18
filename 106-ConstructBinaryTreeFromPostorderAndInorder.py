'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Total Accepted: 53469 Total Submissions: 193965 Difficulty: Medium

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree. 
'''



# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
    	if not inorder or not postorder or len(inorder) != len(postorder):
    		return None
    	root=TreeNode(postorder[-1])
    	nodeStack=[root]


    	nodeOrderDict={inorder[order]:order for order in xrange(len(inorder))}
    	nodeStack.append(root)
    	for val in postorder[-2::-1]:
    		print 'start', val
    		newNode=TreeNode(val)
    		if nodeOrderDict[val]>nodeOrderDict[nodeStack[-1].val]:
    			nodeStack[-1].right=newNode
    			nodeStack.append(newNode)
    			# print val
    		else:
    			attachNode=nodeStack.pop()
    			while nodeStack and nodeOrderDict[nodeStack[-1].val]>nodeOrderDict[val]:
    				attachNode=nodeStack.pop()
    			attachNode.left=newNode
    			nodeStack.append(newNode)
    	return root

if __name__ == '__main__':
	solution=Solution()
	print solution.buildTree([1,3,2],[3,2,1]).val



        