'''
200. Number of Islands
Total Accepted: 33490 Total Submissions: 127909 Difficulty: Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000

Answer: 1

Example 2:

11000
11000
00100
00011

Answer: 3
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        height=1
        stack=[]
        results=[]

        while root or stack:
            if root:
                # append root to stack only when there is a left child.  this is different to when doing in-order transversal.  
                # In here, you use the root value when it is first visited, so you do not have to stack it if there is no future need for it.
                # When doing in-order transversal, you will only use the root value after it gets popped from stack.
                if root.left:
                    # you have to store height as well, since you have skipped unknown number of nodes with no left children
                    stack.append((root,height))
                if height>len(results):
                    results.append(root.val)

                root=root.right
                height+=1
                
            else:
                root,height=stack.pop()
                root=root.left
                height+=1
        return results

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.right=TreeNode(5)
root.right.right=TreeNode(4)
root.right.left=TreeNode(6)
root.right.left.right=TreeNode(7)

print Solution().rightSideView(root)



