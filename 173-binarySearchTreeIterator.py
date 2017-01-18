# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack=[]
        self.root=root
              

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return bool(self.root or self.stack)

    # @return an integer, the next smallest number
    def next(self):
        while self.root or self.stack:
            if self.root:
                self.stack.append(self.root)
                self.root=self.root.left
            else:
                node=self.stack.pop()
                res=node.val
                self.root=node.right
                return res


class BSTIteratorOld:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack=[]
        self.root=root
        while self.root and self.root.left:
            self.stack.append(self.root)
            self.root=self.root.left        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        while self.root:
            return True
        else:
            return False

    # @return an integer, the next smallest number
    def next(self):
        ans=self.root.val
        if self.root.right:
            self.root=self.root.right
            while self.root.left:
                self.stack.append(self.root)
                self.root=self.root.left
        elif self.stack:
            self.root=self.stack.pop()
        else:
            self.root=None
        return ans

if __name__ == '__main__':
	root=TreeNode(1)
	root.right=TreeNode(2)
	iter=BSTIterator(root)

	print iter.hasNext()
	print iter.next()
	print iter.next()
	

