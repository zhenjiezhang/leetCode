'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit.
 Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''


# Definition for singly-linkd list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None




class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
    	frontNode=result=ListNode(0)
    	node1=l1
    	node2=l2
    	carry=0
    	while (node1 or node2):
    		val1=val2=0

    		if node1:
    			val1=node1.val
    			node1=node1.next
    		if node2:
    			val2=node2.val
    			node2=node2.next

    		frontNode.next=ListNode((val1+val2+carry)%10)
    		carry=(val1+val2+carry)/10
    		frontNode=frontNode.next
    		
    	if carry==1:
    		frontNode.next=ListNode(1)
    	return result.next

if __name__=="__main__":
	solution=Solution()
	l1=ListNode(2)
	l1.next=ListNode(9)
	l1.next.next=ListNode(4)

	l2=ListNode(5)
	l2.next=ListNode(5)
	l2.next.next=ListNode(7)

	print solution.addTwoNumbers(l1,l2).val
	print solution.addTwoNumbers(l1,l2).next.val
	print solution.addTwoNumbers(l1,l2).next.next.val
	print solution.addTwoNumbers(l1,l2).next.next.next.val





    	
