class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
# my new solution, two passes technically, but much clearer.
	def reverseKGroup(self, head, k):
		newHead=pre=ListNode(0)
		newHead.next=head

		while True:
			kProbe=pre
			i=0
			while i<k and kProbe.next:
				kProbe=kProbe.next
				i+=1
			if i!=k:
				break

			swapFront=pre.next

			for _ in xrange(k-1):
				pre.next, swapFront.next.next, swapFront.next=swapFront.next, pre.next, swapFront.next.next
			pre=swapFront

		return newHead.next



# old one, to use only one pass
	def reverseKGroupOld(self, head, k):
		newHead=None
		swapHead=None
		lastTail=None
		tempHead=None
		swapedNum=0

		if k<=1:
			return head

		if not head:
			return head


		psudoHead=ListNode(0)
		psudoHead.next=head
		swapHead=psudoHead

		if swapHead.next:
			lastTail=swapHead
			swapHead=swapHead.next
			swapedNum=swapedNum+1

		while swapHead.next and swapedNum <k:
			newNode=swapHead.next
			swapHead.next=newNode.next
			newNode.next=lastTail.next
			lastTail.next=newNode
			swapedNum=swapedNum+1

			if swapedNum == k:
				swapedNum=0
				if swapHead.next:
					lastTail=swapHead
					swapHead=swapHead.next
					swapedNum=swapedNum+1
				else:
					break

		while swapedNum>1:
			newNode=lastTail.next
			lastTail.next=newNode.next
			newNode.next=swapHead.next
			swapHead.next=newNode
			swapedNum=swapedNum-1		


		return psudoHead.next


if __name__=="__main__":
	solution=Solution()
	tail=head=ListNode(1)
	tail.next=tail=ListNode(2)
	tail.next=tail=ListNode(3)
	tail.next=tail=ListNode(4)
	tail.next=tail=ListNode(5)
	tail.next=tail=ListNode(6)
	tail.next=tail=ListNode(7)
	tail.next=tail=ListNode(8)



	node=solution.reverseKGroup(head, 5)

	while (node):
		print (node.val)
		node=node.next





