'''
143. Reorder List
Total Accepted: 57369 Total Submissions: 260301 Difficulty: Medium

Given a singly linked list L: L0 to L1 to...to Ln-1 to Ln
reorder it to: L0 to Ln to L1 to Ln-1 to L2 to Ln-2 to...

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}. 
'''

'''

This way of thinking is ingeneous. should implement it.


public void reorderList(ListNode head){
          if(head == null || head.next == null) return;
          ListNode h = reorderList(head, head,head);
     }

public ListNode reorderList(ListNode prev, ListNode slow, ListNode faster){
    if(faster == null || faster.next == null) {
        if(faster != null) {
            ListNode reverse = slow.next;
            slow.next = null;
            return reverse;
        }
        prev.next = null;
        return slow;
    }
    ListNode retNode = reorderList(slow, slow.next, faster.next.next);
    // concanate
    ListNode temp = retNode.next;
    retNode.next = slow.next;
    slow.next = retNode;
    return temp;
}
'''



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return nothing


    def reorderList(self, head):
        if not head or not head.next:
            return

        # find the two halves
        p1=p2=head
        while p1 and p1.next and p1.next.next:
            p1=p1.next.next
            p2=p2.next

        p1, prep2, p2=head, p2, p2.next

        #reverse the later half
        prep2.next=None
        p2_1=p2
        p2_2=p2.next
        p2.next=None

        while p2_2:
            tmp=p2_2.next
            p2_2.next=p2_1
            p2_1, p2_2=p2_2, tmp

        p2=p2_1

        #merge the two halves
        while p2:
            tmp=p2.next
            p2.next=p1.next
            p1.next=p2
            p1=p2.next
            p2=tmp




            
            # can not write in one line
            # p1, p1.next, prep2.next, p2, p2.next=p1.next, p2, p2.next, p2.next, p1.next




    def reorderListOld(self, head):
        nodes=[]
        while head:
        	nodes.append(head)
        	head=head.next
        attach,tail=0,len(nodes)-1

        while tail>attach+1:
        	nodes[tail].next=nodes[attach].next
        	nodes[attach].next=nodes[tail]
        	tail-=1
        	attach+=1
        
        
        if nodes:
        	nodes[tail].next=None

if __name__ == '__main__':
    s=Solution()
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(3)
    head.next.next.next=ListNode(4)

    s.reorderList(head)
    while head:
        print head.val
        head=head.next
    