'''
24. Swap Nodes in Pairs
Total Accepted: 76618 Total Submissions: 226320 Difficulty: Medium

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        node=self
        string=''
        while node:
            string+=str(node.val)+' '
            node=node.next
        return string

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        prev=token=ListNode(0)
        prev.next=head
        lead=head

        while lead and lead.next:
            # snd=lead.next
            # lead.next=snd.next
            # snd.next=lead
            # prev.next=snd


            prev.next=lead.next
            lead.next=prev.next.next
            prev.next.next=lead


            prev=lead
            lead=lead.next

        return token.next

if __name__=="__main__":
    head=ListNode(1)
    head.next=ListNode(2)
    head.next.next=ListNode(3)
    head.next.next.next=ListNode(4)
    head.next.next.next.next=ListNode(5)

    solution=Solution()
    print solution.swapPairs(head)


