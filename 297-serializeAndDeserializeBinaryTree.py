'''
297. Serialize and Deserialize Binary Tree
Total Accepted: 12094 Total Submissions: 45932 Difficulty: Medium

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless. 
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root==None:
            return '[null]'


        serialStr='['
        nodeList=[root]
        while nodeList:
            newList=[]
            for node in nodeList:
                if node:
                    newList.append(node.left)
                    newList.append(node.right)
                    serialStr+=(str(node.val)+',')
                else:
                    serialStr+='null,'
            nodeList=newList
        return serialStr[:-1]+']'


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        tokens=data[1:len(data)-1].split(',')
        p=0
        root=None if tokens[p]=='null' else TreeNode(int(tokens[p]))
        if not root:
            return root
        p+=1

        nodeList=[root]
        numOfRealNodesInList=0
        while nodeList:
            newList=[]

            for node in nodeList:
                if node:
                    numOfRealNodesInList+=1
                    newNode=None if tokens[p]=='null' else TreeNode(int(tokens[p]))
                    node.left=newNode
                    newList.append(newNode)
                    p+=1

                    newNode=None if tokens[p]=='null' else TreeNode(int(tokens[p]))
                    node.right=newNode
                    newList.append(newNode)
                    p+=1

            nodeList=newList
        return root


if __name__ == '__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=None
    root.left.left=TreeNode(3)
    root.left.right=None
    root.left.left.left=TreeNode(4)
    root.left.left.right=None
    root.left.left.left.left=TreeNode(5)

    codec = Codec()

    r=codec.deserialize(codec.serialize(root))
    # l=codec.deserialize(codec.serialize(None))
    # k=codec.deserialize(codec.serialize(TreeNode(1)))


    print r.left.val
    print r.left.left.val
    print r.left.left.left.val







# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))