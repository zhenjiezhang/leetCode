# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
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

