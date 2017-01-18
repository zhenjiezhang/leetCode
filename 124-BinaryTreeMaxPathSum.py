'''
124. Binary Tree Maximum Path Sum
Total Accepted: 56907 Total Submissions: 252089 Difficulty: Hard

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3

Return 6. 

'''

'''
my question:
how to do it with DP?

'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer

    def maxPathSum(self, root):
        self.maxSum=-float('inf')
        self.maxSumFromNode(root)
        return self.maxSum


    def maxSumFromNode(self, node):
        if not node:
            return 0

        leftPath=max(self.maxSumFromNode(node.left),0)
        rightPath=max(self.maxSumFromNode(node.right),0)

        if node.val+leftPath+rightPath>self.maxSum:
            self.maxSum=node.val+leftPath+rightPath
        
        return node.val+max(leftPath, rightPath)










'''
old
'''


    def maxPathSumOld(self, root):
        if not root:
            return None

        maxSum=-float('inf')


        frontNode=root

        pathStack=[]
        maxSumRootDict={}

        while True:
            
            maxSumRootDict[frontNode]=frontNode.val
            if maxSumRootDict[frontNode]>maxSum:
                maxSum=maxSumRootDict[frontNode]

            if frontNode.left:
                pathStack.append(frontNode)
                frontNode=frontNode.left

            elif frontNode.right:
                pathStack.append(frontNode)
                frontNode=frontNode.right

            else:

                while pathStack and (not pathStack[-1].right or pathStack[-1].right in maxSumRootDict):
                    mother=pathStack.pop()

                    if maxSumRootDict[frontNode]>0:
                        if maxSumRootDict[mother]==mother.val:
                            maxSumRootDict[mother]+=maxSumRootDict[frontNode]
                            if maxSumRootDict[mother]>maxSum:
                                maxSum=maxSumRootDict[mother]
                        else:
                            if maxSumRootDict[frontNode]+maxSumRootDict[mother]>maxSum:
                                maxSum=maxSumRootDict[frontNode]+maxSumRootDict[mother]
                            if maxSumRootDict[frontNode]+mother.val>maxSumRootDict[mother]:
                                maxSumRootDict[mother]=maxSumRootDict[frontNode]+mother.val

                    frontNode=mother
                if pathStack:
                    mother=pathStack[-1]
                    if maxSumRootDict[frontNode]>0:
                        maxSumRootDict[mother]+=maxSumRootDict[frontNode]
                        if maxSumRootDict[mother]>maxSum:
                            maxSum=maxSumRootDict[mother]
                    frontNode=mother.right
                else:
                    return maxSum





            

if __name__ == '__main__':
    solution=Solution()
    root=TreeNode(-1)
    root.left=TreeNode(-2)
    root.right=TreeNode(-3)
    root.left.left=TreeNode(1)
    root.left.right=TreeNode(3)
    root.right.left=TreeNode(-2)
    root.left.left.left=TreeNode(-1)

    root1=TreeNode(1)
    root1.left=TreeNode(2)
    root1.right=TreeNode(3)


    print solution.maxPathSum(root)
    print solution.maxPathSumOld(root)




