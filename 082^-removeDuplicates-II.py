'''
82. Remove Duplicates from Sorted List II
Total Accepted: 62070 Total Submissions: 238277 Difficulty: Medium

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        first=ListNode(0)
        first.next=head
        upstream=first
        probe=head

        while probe:
            if probe.next and probe.next.val==probe.val:
                while probe.next and probe.next.val==probe.val:
                    probe=probe.next
                upstream.next=probe.next
                probe=probe.next
            else:
                upstream=probe
                probe=probe.next
        return first.next