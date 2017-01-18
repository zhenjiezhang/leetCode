# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedArrayToBST(self,num):
    	if not num:
    		return None
    	root=TreeNode(num[len(num)/2])
    	root.left=self.sortedArrayToBST(num[:len(num)/2])
    	root.right=self.sortedArrayToBST(num[len(num)/2+1:])
    	return root


    def sortedListToBST(self, head):
    	num=[]
    	while head:
    		num.append(head.val)
    		head=head.next
    	if num:
    		return self.sortedArrayToBST(num)
    	else:
    		return None
    		
if __name__ == '__main__':
	solution=Solution()
	print solution.sortedArrayToBST([1,2,3]).val