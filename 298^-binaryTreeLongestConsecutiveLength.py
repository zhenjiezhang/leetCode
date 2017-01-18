'''
simpler version:
public class Solution {
    public int longestConsecutive(TreeNode root) {
        return (root==null)?0:Math.max(dfs(root.left, 1, root.val), dfs(root.right, 1, root.val));
    }

    public int dfs(TreeNode root, int count, int val){
        if(root==null) return count;
        count = (root.val - val == 1)?count+1:1;
        int left = dfs(root.left, count, root.val);
        int right = dfs(root.right, count, root.val);
        return Math.max(Math.max(left, right), count);
    }
}
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.maxLength=0

    def longestConsecutive(self, root, length=1):
        if not root:
            return 0
        if root.left and root.left.val==root.val+1:
            self.longestConsecutive(root.left, length+1)
        else:
            self.longestConsecutive(root.left, 1)
            self.maxLength=max(self.maxLength, length)
        if root.right and root.right.val==root.val+1:
            self.longestConsecutive(root.right, length+1)
        else:
            self.longestConsecutive(root.right,1)
            self.maxLength=max(self.maxLength, length)
        return self.maxLength







    def longestConsecutiveOld(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLength=0
        if root:
            self.startStack=[root]
            while self.startStack:
                self.followPath(1,self.startStack.pop())
        return self.maxLength

    def followPath(self, currentLength, probe):
        thisLength=currentLength
        if probe.left and probe.left.val!=probe.val+1:
            self.startStack.append(probe.left)
        if probe.right and probe.right.val!=probe.val+1:
            self.startStack.append(probe.right)

        if (not probe.left or probe.left.val!=probe.val+1) and (not probe.right or probe.right.val!=probe.val+1):
            if currentLength>self.maxLength:
                self.maxLength=currentLength

        if probe.left and probe.left.val==probe.val+1:
            self.followPath(currentLength+1, probe.left)

        if probe.right and probe.right.val==probe.val+1:
            self.followPath(currentLength+1, probe.right)

if __name__ == '__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.left.left=TreeNode(3)
    root.left.right=TreeNode(3)
    root.left.right.left=TreeNode(4)

    root.right=TreeNode(3)
    root.right.left=TreeNode(4)
    root.right.left.left=TreeNode(5)
    root.right.left.left.right=TreeNode(6)
    root.right.left.left.right.right=TreeNode(7)


    solution=Solution()
    print solution.longestConsecutive(root)
    print solution.longestConsecutiveOld(root)


