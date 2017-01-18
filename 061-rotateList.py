'''
61. Rotate List
Total Accepted: 57863 Total Submissions: 259573 Difficulty: Medium

Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
    	string=''
    	head=self
    	while head:
    		string+=str(head.val)
    		head=head.next

    	return string

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
    	

    	length=0    	
    	last=first=head


    	while first:
    		last=first
    		first=first.next
    		length+=1

    	if length<2 or k==0:
    		return head

            

    	k=k%length
    	if k==0:
    		return head

    	pre=first=head
    	count=0
        while count<(length-k):
        	pre=first
        	first=first.next
        	count+=1

        pre.next=last.next
        last.next=head
        head=first

        return head

if __name__=="__main__":
	solution=Solution()
	head=ListNode(1)
	head.next=ListNode(2)
	# head.next.next=ListNode(3)
	# head.next.next.next=ListNode(4)
	# head.next.next.next.next=ListNode(5)

	print solution.rotateRight(head,2)







