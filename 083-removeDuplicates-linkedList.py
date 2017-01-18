'''
83. Remove Duplicates from Sorted List
Total Accepted: 95243 Total Submissions: 266251 Difficulty: Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode

    # the old one is suprisingly better.  

    def deleteDuplicates(self, head):
        probe=head
        while probe:
            if probe.next and probe.next.val==probe.val:
                start=probe
                probe=probe.next
                while probe.next and probe.next.val==probe.val:
                    probe=probe.next
                start.next=probe.next

            probe=probe.next
        return head


    def deleteDuplicatesOld(self, head):
    	probe=head
    	while probe:
    		while probe.next and probe.next.val==probe.val:
    			probe.next=probe.next.next
    		probe=probe.next
    	return head


        