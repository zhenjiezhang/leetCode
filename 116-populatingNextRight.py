'''
116. Populating Next Right Pointers in Each Node
Total Accepted: 75526 Total Submissions: 207557 Difficulty: Medium

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }

Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

    You may only use constant extra space.
    You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,
Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

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
    def connect(self, root):
    	if root==None:
    		return None

        root.next=None
        layerStart=root        

        while layerStart.left:

            currentNode=layerStart
            
            while currentNode:
                currentNode.left.next=currentNode.right
                currentNode.right.next=currentNode.next.left if currentNode.next else None
                currentNode=currentNode.next

            layerStart=layerStart.left


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


        





        