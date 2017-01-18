'''
86. Partition List
Total Accepted: 56263 Total Submissions: 197266 Difficulty: Medium

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5. 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
    	head=self
    	string=""
    	while head:
    		string+=str(head.val)
    		head=head.next
    	return string

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
    	psdHead=ListNode(0)
    	psdHead.next=head

    	interPoint=psdHead
    	while interPoint.next and interPoint.next.val<x:
    		interPoint=interPoint.next
    	probe=interPoint

    	while probe and probe.next:
    		# print probe.next.val,interPoint.next.val
    		if probe.next.val<x:
    			tmp=interPoint.next
    			interPoint.next=probe.next
    			probe.next=interPoint.next.next
    			interPoint.next.next=tmp
    			interPoint=interPoint.next
    		else:
    			probe=probe.next

    	return psdHead.next

    def nodeList(self, vals):
    	head=probe=ListNode(0)
    	for n in vals:
    		probe.next=ListNode(n)
    		probe=probe.next
    	return head.next




if __name__ == '__main__':
	head=Solution().nodeList([1,4,3,2,1,5,6,2])
	# print(head)
	print (Solution().partition(head,3))




        