'''
92. Reverse Linked List II
Total Accepted: 60974 Total Submissions: 226228 Difficulty: Medium

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list. 
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
    	if m==n:
    		return head
    	psdHead=ListNode(0)
    	psdHead.next=head
    	breakNode=psdHead
    	for i in xrange(m-1):
    		breakNode=breakNode.next

    	firstRev=breakNode.next
    	revFront=firstRev.next
    	firstRev.next=revFront.next
    	revFront.next=firstRev

    	for i in xrange(n-m-1):
    		tmp=firstRev.next.next
    		firstRev.next.next=revFront
    		revFront=firstRev.next
    		firstRev.next=tmp

    	breakNode.next=revFront

        return psdHead.next


        