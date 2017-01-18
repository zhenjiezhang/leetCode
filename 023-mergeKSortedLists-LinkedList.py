import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
	def mergeKLists(self, heads):
		heap=[]
		k=len(heads)

		for head in heads:
			if (head):
				heapq.heappush(heap,(head.val, head))
		newHead=newTail=ListNode(0)

		while (heap):
			newTail.next=(heapq.heappop(heap))[1]
			newTail=newTail.next
			if (newTail.next):
				heapq.heappush(heap,(newTail.next.val, newTail.next))
		return newHead.next

if __name__=="__main__":
	solution=Solution()

	heads=[ListNode(1),ListNode(4),ListNode(2),ListNode(2)]
	tails=list(heads)
	tails[0].next=tails[0]=ListNode(6)
	tails[1].next=tails[1]=ListNode(5)
	tails[2].next=tails[2]=ListNode(3)
	tails[3].next=tails[3]=ListNode(4)
	# tails[0]=tails[0].next
	# tails[1]=tails[1].next
	# tails[2]=tails[2].next
	# tails[3]=tails[3].next
	tails[0].next=tails[0]=ListNode(7)
	tails[1].next=tails[1]=ListNode(8)
	tails[2].next=tails[2]=ListNode(4)
	tails[3].next=tails[3]=ListNode(4)


	node=solution.mergeKLists(heads)

	while (node):
		print (node.val)
		node=node.next