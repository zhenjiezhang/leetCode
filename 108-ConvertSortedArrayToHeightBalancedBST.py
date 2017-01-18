'''
108. Convert Sorted Array to Binary Search Tree
Total Accepted: 64333 Total Submissions: 179227 Difficulty: Medium

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param num, a list of integers
    # @return a tree node

    def sortedArrayToBST(self,num):
        if not num:
            return None
        root=TreeNode(num[len(num)/2])
        root.left=self.sortedArrayToBST(num[:len(num)/2])
        root.right=self.sortedArrayToBST(num[len(num)/2+1:])
        return root

        


    def sortedArrayToBST(self, num):
        n=len(num)
        d1=1
        while n>>d1:
            d1+=1
        d2=d1-1

        rootIndex=2**(d1-1)-1 if (1<<d2&n) else 2**(d1-2)+n-(2**(d1-1)-1)







    def sortedArrayToBSTOld(self, num):
    	if not num:
    		return None
        height=1
        while 2**height-1<len(num):
            height+=1
        if height==1:
        	return TreeNode(num[0])
        resNum=len(num)-2**(height-1)+1
        if resNum>=2**(height-2):
            leftNum=2**(height-1)-1

        else:
            leftNum=2**(height-2)-1+resNum




        leftNum=int(leftNum)
        # print num[leftNum]
        root=TreeNode(num[leftNum])
        root.left=self.sortedArrayToBST(num[:leftNum])
        root.right=self.sortedArrayToBST(num[leftNum+1:])
        return root

if __name__ == '__main__':
    solution=Solution()
    print solution.sortedArrayToBST([1,3]).val




        