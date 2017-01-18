# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
    	fast=slow=head
    	n=0
    	while slow and slow.next:
    		fast=fast.next
    		slow=slow.next.next
    		n+=1
    		if fast==slow:
    			n=1
    			fast=fast.next
    			slow=slow.next.next
    			while fast!=slow:
    				fast=fast.next
    				slow=slow.next.next
    				n+=1
    			break

    	if slow and slow.next:
    		tail=head
            # you do not have to move to there, because fast and slow are already there!
    		for i in xrange(n):
    			tail=tail.next
    		while head!=tail:
    			head=head.next
    			tail=tail.next

    		return head
    	else:
    		return None

if __name__ == '__main__':
	solution=Solution()
	head=ListNode(1)
	head.next=ListNode(2)
	head.next.next=ListNode(3)
	head.next.next.next=ListNode(4)
	head.next.next.next.next=ListNode(5)
	head.next.next.next.next.next=head.next
	print solution.detectCycle(head).val

# The following is better:
# ListNode *detectCycle(ListNode *head) {
#     if (head == NULL || head->next == NULL)
#         return NULL;

#     ListNode *slow  = head;
#     ListNode *fast  = head;
#     ListNode *entry = head;

#     while (fast->next && fast->next->next) {
#         slow = slow->next;
#         fast = fast->next->next;
#         if (slow == fast) {                      // there is a cycle
#             while(slow != entry) {               // found the entry location
#                 slow  = slow->next;
#                 entry = entry->next;
#             }
#             return entry;
#         }
#     }
#     return NULL;                                 // there has no cycle
# }