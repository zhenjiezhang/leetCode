'''
112. Path Sum
Total Accepted: 85995 Total Submissions: 281117 Difficulty: Easy

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1

return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
'''
you can practice inorder traversal dfs, or bfs using level down.
'''


# Definition for a  binary trese node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def existPath(self,root,sum):
        if sum<0:
            return False
            
    	if not root:
    		return sum==0

    	if not (root.left or root.right):
    		if root.val==sum:
    			return True    	
    		else:
    			return False

    	return root.left is not None and self.existPath(root.left,sum-root.val) or (root.right is not None and self.existPath(root.right,sum-root.val))
    	

    def hasPathSum(self, root, sum):

    	if not root:
    		return False
    	else:
    		return self.existPath(root,sum)

if __name__ == '__main__':
	solution=Solution()
	root=TreeNode(1)
	root.right=TreeNode(2)
	print solution.hasPathSum(root,2)

        