'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Total Accepted: 53469 Total Submissions: 193965 Difficulty: Medium

Given preorder and inorder traversal of a tree, construct the binary tree.
Note:
You may assume that duplicates do not exist in the tree. 

'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        self.preorder=preorder
        self.inorder=inorder

        return self.recurse(0, len(preorder), 0, len(inorder))
    def recurse(self, preStart, preEnd, inStart, inEnd):
        if preStart>=preEnd:
            return None

        root=TreeNode(self.preorder[preStart])
        rootIndex=self.inorder.index(self.preorder[preStart])

        root.left=self.recurse(preStart+1, preStart+rootIndex-inStart+1, inStart, rootIndex)
        root.right=self.recurse(preStart+rootIndex-inStart+1, preEnd, rootIndex+1, inEnd)
        return root



    def buildTreeOld(self, preorder, inorder):
        if not preorder:
            return None
        searchTreeDict=dict()
        for i in xrange(len(inorder)):
            searchTreeDict[inorder[i]]=[i]

        root=TreeNode(preorder[0])
        upStack=[]
        upStack.append(root)
        for val in preorder[1:]:
            searchTreeVal=searchTreeDict[val]
            newNode=TreeNode(val)
            if searchTreeVal < searchTreeDict[upStack[-1].val]:
                upStack[-1].left=newNode
                upStack.append(newNode)
            else:
                attachNode=upStack.pop()
                while upStack and searchTreeVal > searchTreeDict[upStack[-1].val]:
                    attachNode=upStack.pop()
                attachNode.right=newNode
                upStack.append((newNode))
        return root

if __name__ == '__main__':
    solution=Solution()
    print solution.buildTreeOld([1,2],[2,1]).left.val



