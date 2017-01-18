'''
95. Unique Binary Search Trees II
Total Accepted: 47470 Total Submissions: 164848 Difficulty: Medium

Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

   '''


'''
recursive is a bit of trivial.  This is a good implementation:

def node(val, left, right):
    node = TreeNode(val)
    node.left = left
    node.right = right
    return node

class Solution:
    def generateTrees(self, last, first=1):
        return [node(root, left, right)
                for root in range(first, last+1)
                for left in self.generateTrees(root-1, first)
                for right in self.generateTrees(last, root+1)] or [None]

'''


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None





class Solution:
    # @return a list of tree node

    def treeNumSubstitution(self, root,numList):
        if root is None:
            return None
        newRoot=TreeNode(numList[root.val-1])
        if root.left:
            newRoot.left=self.treeNumSubstitution(root.left,numList)
        if root.right:
            newRoot.right=self.treeNumSubstitution(root.right,numList)
        return newRoot

    def generateTrees(self, n):
        if n==0:
            return []
        num2Trees=dict()
        num2Trees[0]=[None]
        for i in xrange(1,n+1):
            num2Trees[i]=[]
            for rootPos in xrange(1,i+1):
                for leftTree in num2Trees[rootPos-1]:
                    for rightTree in num2Trees[i-rootPos]:
                        root=TreeNode(rootPos)
                        num2Trees[i].append(root)
                        rightTree=self.treeNumSubstitution(rightTree,range(rootPos+1,i+1))
                        root.left=leftTree
                        root.right=rightTree
        # print num2Trees[n]
        return num2Trees[n]

if __name__ == '__main__':
    solution=Solution()
    root=solution.generateTrees(3)
    print len(root)
    root=solution.generateTrees(0)

    # print  root[0].val,root[0].right.val
    # print  root[1].val,root[1].left.val


