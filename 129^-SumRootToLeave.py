# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if not root:
            return 0
        self.results=0
        self.dfs(root)
        return self.results

    # directly compute the numerical reesults, instead of saving path into list or string.
    def dfs(self, root, partialSum=0):
        partialSum=partialSum*10+root.val
        if not root.left and not root.right:
            self.results+=partialSum
            return
        if root.left:
            self.dfs(root.left, partialSum)
        if root.right:
            self.dfs(root.right, partialSum)






    def dfs_v1(self, root, path=[]):

        path.append(root.val)
        if not root.left and not root.right:
            self.results+=reduce(lambda x, y: x*10+y, path)
            path.pop()
            return

        if root.left:
            self.dfs(root.left, path)
        if root.right:
            self.dfs(root.right, path)

        path.pop()








    def findAllNumbers(self,root):
        #return a list of all numbers constructed from root to leaves
        results=[]
        if not root:
            return []

        if (not root.left) and (not root.right):
            return [str(root.val)]


        if root.left:
            lResults=self.findAllNumbers(root.left)
            results+=[str(root.val)+lResult for lResult in lResults]

        if root.right:
            rResults=self.findAllNumbers(root.right)
            results+=[str(root.val)+rResult for rResult in rResults]
        return results





    def sumNumbersOld(self, root):
        return sum([int(result) for result in self.findAllNumbers(root)])


if __name__ == '__main__':
    solution=Solution()
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(9)
    print solution.sumNumbers(root)

        