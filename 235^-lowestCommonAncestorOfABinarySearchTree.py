# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        r=root

        vp,vq=p.val,q.val

        while r:
        	if (r.val-vp)*(r.val-vq)>0:
        		r=r.left if r.val>=vp else r.right
        	elif (r.val-vp)*(r.val-vq)<0:
        		return r

if __name__=="__main__":
	s=Solution()
	root=TreeNode(6)
	root.left=TreeNode(2)
	root.right=TreeNode(8)
	root.left.left=TreeNode(0)
	root.left.right=TreeNode(4)

	print s.lowestCommonAncestor(root,root,root.left).val


