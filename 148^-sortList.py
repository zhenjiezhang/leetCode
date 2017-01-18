'''
148. Sort List
Total Accepted: 62684 Total Submissions: 262402 Difficulty: Medium

Sort a linked list in O(n log n) time using constant space complexity.



I should do a quick search as well?


'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def mergeSortList(self, head, n):
    	if n==1:
    		return head
    	iead=head
    	for i in xrange(n/2-1):
    		iead=iead.next
    	secondStart=iead.next
    	iead.next=None


    	firstHead=self.mergeSortList(head,n/2)
    	secondHead=self.mergeSortList(secondStart,n-n/2)
    	gead=tail=ListNode(0)
        while firstHead and secondHead:
        	# print firstHead.val, secondHead.val
        	if firstHead.val<=secondHead.val:
        		tail.next=firstHead
        		firstHead=firstHead.next
        	else:
        		tail.next=secondHead
        		secondHead=secondHead.next
        	tail=tail.next

        # you can write it this way instead of a test:    
        tail.next=firstHead or secondHead

        return gead.next



    def sortList(self, head):
    	if not head:
    		return None
    	count=0
    	pointer=head
    	while pointer:
    		count+=1
    		pointer=pointer.next
    	return self.mergeSortList(head,count)


if __name__ == '__main__':
	solution=Solution()
	head=ListNode(5)
	head.next=ListNode(4)
	head.next.next=ListNode(1)
	head.next.next.next=ListNode(9)
	head.next.next.next.next=ListNode(2)
	print solution.sortList(head).next.val

        