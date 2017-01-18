'''
114. Flatten Binary Tree to Linked List
Total Accepted: 71015 Total Submissions: 236281 Difficulty: Medium

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6

The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

click to show hints.
Hints:

If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        waitingList=[]
        curNode=root

        while curNode or waitingList:
            if curNode.left:
                if curNode.right:
                    waitingList.append(curNode.right)

                curNode.right=curNode.left
                curNode.left=None

            elif not curNode.right:
                if waitingList:
                    curNode.right=waitingList.pop()
                else:
                    return 
            curNode=curNode.right



if __name__ == '__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)

    solution=Solution()
    solution.flatten(root)
    print root.val, root.right.val, root.right.right.val



        