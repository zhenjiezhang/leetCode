'''278. First Bad Version
Total Accepted: 30729 Total Submissions: 140937 Difficulty: Easy

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API. 
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        self.rightStack=[]
        self.leftStack=[]
        self.left=self.right=targetNode=None

        result=[]
        probe=root

        while probe:
            if probe.val > target:
                self.rightStack.append(probe)
                probe=probe.left
            elif probe.val < target:
                self.leftStack.append(probe)
                probe=probe.right
            else:
                targetNode=probe
                break

        if targetNode:
            result.append(targetNode.val)
            self.left=self.right=targetNode
            self.nextLeft()
            self.nextRight()

        else:
            self.left=self.leftStack.pop() if self.leftStack else None
            self.right=self.rightStack.pop() if self.rightStack else None

        lv=self.nextLeft() if self.left else -float('inf')
        rv=self.nextRight() if self.right else float('inf')


        while len(result)<k:
            if abs(lv-target)<abs(rv-target):
                result.append(lv)
                lv=self.nextLeft() if self.left else -float('inf')
                

            else:
                result.append(rv)
                rv=self.nextRight() if self.right else float('inf')

        return result

    def nextLeft(self):
        value=self.left.val

        if self.left.left:
            self.left=self.left.left
            while self.left.right:
                self.leftStack.append(self.left)
                self.left=self.left.right
        elif self.leftStack:
            self.left=self.leftStack.pop()
        else:
            self.left=None
        return value

    def nextRight(self):
        value=self.right.val


        if self.right.right:
            self.right=self.right.right
            while self.right.left:
                self.rightStack.append(self.right)
                self.right=self.right.left
        elif self.rightStack:
            self.right=self.rightStack.pop()
        else:
            self.right=None
        return value



        

if __name__ == '__main__':
    root=TreeNode(1)
    root.right=TreeNode(2)
    # root.right=TreeNode(12)
    # root.left.left=TreeNode(1)

    solution=Solution()
    print solution.closestKValues(root, 3.1, 1)
