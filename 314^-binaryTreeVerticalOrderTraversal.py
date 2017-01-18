'''314. Binary Tree Vertical Order Traversal
Total Accepted: 1351 Total Submissions: 4587 Difficulty: Medium

Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its vertical order traversal as:

[
  [9],
  [3,15],
  [20],
  [7]
]

Given binary tree [3,9,20,4,5,2,7],

    _3_
   /   \
  9    20
 / \   / \
4   5 2   7

return its vertical order traversal as:

[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]

'''
'''
I've considered too much, this is a simpler solution:

def verticalOrder(self, root):
    cols = collections.defaultdict(list)
    queue = [(root, 0)]
    for node, i in queue:
        if node:
            cols[i].append(node.val)
            queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]


Same to my second thoughts
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        self.rightCount=[]
        self.numCount=0

        self.traverse(root)

        rightCount=sorted(self.rightCount)

        rightTurn=rightCount[0][0]
        # print rightCount

        result=[]
        i=0
        while i <len(rightCount):
            result.append([])
            while i < len(rightCount) and rightCount[i][0]==rightTurn:
                result[-1].append(rightCount[i][3])
                i+=1

            if i<len(rightCount):
                rightTurn=rightCount[i][0]

        return result


    def traverse(self, root, rightTurn=0, level=0):
        if root.left:
            self.traverse(root.left, rightTurn=rightTurn-1, level=level+1)

        self.rightCount.append([rightTurn, level, self.numCount, root.val])
        self.numCount+=1

        if root.right:
            self.traverse(root.right, rightTurn=rightTurn+1, level=level+1)

if __name__ == '__main__':
    s=Solution()
    root=TreeNode(3)
    root.left=TreeNode(9)
    root.right=TreeNode(20)
    root.left.left=TreeNode(4)
    root.left.right=TreeNode(5)

    root.right.left=TreeNode(2)
    root.right.right=TreeNode(7)


    print s.verticalOrder(root)


