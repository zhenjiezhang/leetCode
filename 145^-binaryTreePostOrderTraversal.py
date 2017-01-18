# use a stack. either do node-right-left, then reverse the result, or do the farthest left leaf, than pop and repeat

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
postorder is the reverse of rightFirst-preorder

you can do it this way too:
ans, stack = [], [root]
    while stack:
        tmp = stack.pop()
        if tmp:
            ans.append(tmp.val)
            stack.append(tmp.left)
            stack.append(tmp.right)
    return ans[::-1]

'''
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        nodeStack=[]
        results=[]
        while root or nodeStack:
            if root:
                results.append(root.val)
                nodeStack.append(root)
                root=root.right
            else:
                root=nodeStack.pop().left
        return results[::-1] if len(results)>1 else results



        







    def postorderTraversalOld(self, root):

        parents=[]
        values=[]
        revertFlag=False
        childrenDone=False
        current=root

        while current:
            if not revertFlag:
                if current.left:
                    parents.append(current)
                    current=current.left
                    continue
                if current.right:
                    parents.append(current)
                    current=current.right
                    continue

                values.append(current.val)

                if parents:
                    revertFlag=True
                    parent=parents.pop()
                    if parent.right==current:
                        childrenDone=True
                    current=parent
                    continue
                break
            else:
                if childrenDone:
                    values.append(current.val)
                    if parents:
                        parent=parents.pop()
                        if parent.left==current:
                            childrenDone=False
                        current=parent
                        continue

                    else:
                        break
                else:
                    if current.right:
                        parents.append(current)
                        current=current.right
                        revertFlag=False
                        continue
                    else:
                        values.append(current.val)
                        if parents:
                            parent=parents.pop()
                            if parent.right==current:
                                childrenDone=True
                            current=parent
                            continue
                        else:
                            break
        return values

if __name__=="__main__":
    solution=Solution()
    root=TreeNode(1)
    root.left=rl=TreeNode(2)
    # root.right=rr=TreeNode(5)
    # rl.left=rll=TreeNode(3)
    rl.right=rlr=TreeNode(4)
    # rr.left=rrl=TreeNode(6)
    # rr.right=rrr=TreeNode(7)

    rl.right.left=TreeNode(5)

    print solution.postorderTraversal(root)
    print solution.postorderTraversalOld(root)
