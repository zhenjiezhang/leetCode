'''
103. Binary Tree Zigzag Level Order Traversal
Total Accepted: 51416 Total Submissions: 186275 Difficulty: Medium

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]


'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        level=[root]
        result=[]
        reverse=False


        while level:
            vals=[]
            newLevel=[]

            for node in level:
                vals.append(node.val)

                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)

            level=newLevel
            result.append(vals[::-1] if reverse else vals)
            reverse=(not reverse)
        return result






    def zigzagLevelOrderOld(self, root):
        if root is None:
            return []

        currentLevel=[]
        nextLevel=[root]
        reverse=False
        results=[]

        while nextLevel:
            currentLevel=nextLevel
            nextLevel=[]
            result=[]

            

            for node in currentLevel[::-1]:
            	result.append((node.val))
            	if not reverse:
        	        node1=node.left
        	        node2=node.right
            	else:
            	    node1=node.right
            	    node2=node.left
                

                if node1:
                    nextLevel.append(node1)
                if node2:
                    nextLevel.append(node2)
            results.append(result)
            reverse=(not reverse)
        return results

if __name__ == '__main__':
    solution=Solution()
    root=TreeNode(3)
    root.left=TreeNode(9)
    root.right=TreeNode(20)
    print solution.zigzagLevelOrder(root)





