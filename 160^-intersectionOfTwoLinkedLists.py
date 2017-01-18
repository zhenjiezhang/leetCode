'''
160. Intersection of Two Linked Lists
Total Accepted: 59275 Total Submissions: 197707 Difficulty: Easy

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.

    '''
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode


    # the following code is a very elegant way of implementing what I initailly contrived:
    # go through of A and B to the end.  If the ends are the same, then they have intersection.
    # now, you know the steps in A, say sA, and steps in B, sB.
    # if sA is longer, then for a second round, you go extra (sA-sB) steps in A first, now A and B are 
    # the same distance to the interaction point.  You go through A and B together and the will meet as the intersection.

    def getIntersectionNode(self, headA, headB):
    	pA,pB=headA,headB
    	if not pA or not pB:
    		return None
        while pA!=pB:
        	if not (oA.next or pB.next):
        		return None
        	pA=pA.next if pA.next else headB
        	pB=pB.next if pB.next else headA
        return pA

