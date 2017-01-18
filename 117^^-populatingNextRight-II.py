'''
117. Populating Next Right Pointers in Each Node II
Total Accepted: 53458 Total Submissions: 164576 Difficulty: Hard

Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

    You may only use constant extra space.

For example,
Given the following binary tree,

         1
       /  \
      2    3
     / \    \
    4   5    7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

    '''


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def makeLeft(self,parent,left):
    	if parent.right:
    		left.next=parent.right
    		return
        
    	self.makeRight(parent, left)




    def makeRight(self,parent,right):

    	while parent.next:

    		parent=parent.next
    		if parent.left:
    			right.next=parent.left
    			return
    		elif parent.right:
    			right.next=parent.right
    			return

    	right.next=None


    def connect(self, root):

    	if not root:
    		return None

    	root.next=None
    	nextLayer=root
    	while (nextLayer):
    		currentNode=nextLayer
    		nextLayer=None
    		

    		while currentNode:
    			if currentNode.left:
    				self.makeLeft(currentNode,currentNode.left)
    				if not nextLayer:
    				    nextLayer=currentNode.left

    			if currentNode.right:
    				self.makeRight(currentNode,currentNode.right)
    				if not nextLayer:
    				    nextLayer=currentNode.right

    			currentNode=currentNode.next

    	return root


if __name__=="__main__":
    solution=Solution()
    root=TreeNode(0)
    root.left=TreeNode(1)
    root.right=TreeNode(2)
    root.left.left=TreeNode(3)
    root.left.right=TreeNode(4)
    root.right.left=TreeNode(5)
    root.right.right=TreeNode(6)

    solution.connect(root)

    node=root.left.left
    while (node.next):
        print node.val
        node=node.next
    print node.val



    	
        