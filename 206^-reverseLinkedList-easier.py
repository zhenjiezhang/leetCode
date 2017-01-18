'''
206. Reverse Linked List
Total Accepted: 78333 Total Submissions: 208630 Difficulty: Easy

Reverse a singly linked list.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        next=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return next






    def reverseListOld(self, head):

        if not head or not head.next:
            return head

        p1,p2,p3=head,head.next,head.next.next
        p1.next=None

        while p3:
            p2.next=p1
            p1=p2
            p2=p3
            p3=p3.next

        p2.next=p1
        return p2
if __name__ == '__main__':
    ln1=ListNode(1)
    ln1.next=ListNode(2)

    r=Solution().reverseList(ln1)
    print r.val



        
        