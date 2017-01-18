'''

141. Linked List Cycle
Total Accepted: 89702 Total Submissions: 244142 Difficulty: Medium

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space? 



'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        fast,slow=head,head
        while slow and slow.next:
            fast=fast.next
            slow=slow.next.next
            if fast==slow:
                return True
        return False

