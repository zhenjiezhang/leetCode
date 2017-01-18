'''
144. Binary Tree Preorder Traversal
Total Accepted: 103442 Total Submissions: 269132 Difficulty: Medium

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3

return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
'''

# using a stack would have been much simpler!


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):

        nodeStack=[]
        results=[]
        while root or nodeStack:
            if not root:
                root=nodeStack.pop().right
                continue
            results.append(root.val)
            nodeStack.append(root)
            root=root.left
        return results














    def preorderTraversalOld(self, root):

    	parents=[]
    	values=[]
    	revertFlag=False
    	childrenDone=False
    	current=root

    	while current:
    		if not revertFlag:
    			values.append(current.val)
    			if current.left:
    				parents.append(current)
    				current=current.left
    				continue
    			if current.right:
    				parents.append(current)
    				current=current.right
    				continue
    			if parents:
    				revertFlag=True
    				parent=parents.pop()
    				if parent.right==current:
    					childrenDone=True
    				current=parent
    				continue
    			break
    		else:
    			if childrenDone:
    				if parents:
    					parent=parents.pop()
    					if parent.left==current:
    						childrenDone=False
    					current=parent
    					continue

    				else:
    					break
    			else:
    				if current.right:
    					parents.append(current)
    					current=current.right
    					revertFlag=False
    					continue
    				else:
    					if parents:
    						parent=parents.pop()
    						if parent.right==current:
    							childrenDone=True
    						current=parent
    						continue
    					else:
    						break
        return values

if __name__=="__main__":
	solution=Solution()
	root=TreeNode(1)
	root.left=rl=TreeNode(2)
	root.right=rr=TreeNode(5)
	# rl.left=rll=TreeNode(3)
	# rl.right=rlr=TreeNode(4)
	# rr.left=rrl=TreeNode(6)
	# rr.right=rrr=TreeNode(7)

	print solution.preorderTraversal(root)


    		

        