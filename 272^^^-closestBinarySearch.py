'''
272. Closest Binary Search Tree Value II
Total Accepted: 4274 Total Submissions: 13666 Difficulty: Hard

Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

    Given target value is a floating point.
    You may assume k is always valid, that is: k ≤ total nodes.
    You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

Hint:

    Consider implement these two helper functions:
        getPredecessor(N), which returns the next smaller node to N.
        getSuccessor(N), which returns the next larger node to N.
    Try to assume that each node has a parent pointer, it makes the problem much easier.
    Without parent pointer we just need to keep track of the path from the root to the current node using a stack.
    You would need two stacks to track the path in finding predecessor and successor node separately.

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
        stack=[]
        values=[]

        probe=root
        self.p1=self.p2=0


        def kregion(v):
            values.append(v)
            if len(values)==k:
                self.p2=k-1
                return False
            elif len(values)>k:
                if abs(values[-1]-target)<abs(values[self.p1]-target):
                    self.p1+=1
                    self.p2+=1
                    return False
                else:
                    return True
        
        while probe or stack:
            if probe:
                stack.append(probe)
                probe=probe.left
            else:
                probe=stack.pop()
                if kregion(probe.val):
                    break
                probe=probe.right
                
        return values[self.p1:self.p2+1]




class SolutionFaster(object):
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



        